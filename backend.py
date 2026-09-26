"""
FastAPI Backend for Google STEP & Microsoft Explore DSA Tracker
Provides REST API for:
- Progress persistence (JSON storage)
- Daily streak & activity heat-matrix calculation
- Intelligent Missed Days & Long Gap Recovery Engine (Ebbinghaus decay analysis)
- Schedule recalibration
"""

from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime, date, timedelta
import json
import os

app = FastAPI(title="Google DSA Tracker API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = os.path.join(os.path.dirname(__file__), "dsa_progress.json")
HTML_FILE = os.path.join(os.path.dirname(__file__), "tracker.html")

TOTAL_PROBLEMS = 57

def load_data() -> dict:
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "solved": [],
        "bookmarks": [],
        "revisits": {},
        "activity": {},
        "start_date": datetime.now().strftime("%Y-%m-%d"),
        "pace": 2,
        "theme": "dark"
    }

def save_data(data: dict):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

class StatePayload(BaseModel):
    solved: List[int] = []
    bookmarks: List[int] = []
    revisits: Dict[str, Any] = {}
    activity: Dict[str, List[int]] = {}
    start_date: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    pace: int = 2
    theme: str = "dark"

class RecalibratePayload(BaseModel):
    mode: str = "from_today"  # 'from_today' or 'shift_days'
    shift_days: int = 0

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
  <path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.66 0 6.58 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/>
  <path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/>
  <path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.28-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/>
  <path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.58 42.62 14.66 48 24 48z"/>
</svg>"""

@app.get("/favicon.ico")
def serve_favicon():
    return Response(content=FAVICON_SVG, media_type="image/svg+xml")

@app.get("/")
def serve_index():
    if os.path.exists(HTML_FILE):
        return FileResponse(HTML_FILE)
    return HTMLResponse("<h1>DSA Tracker HTML file not found</h1>")

@app.get("/api/state")
def get_state():
    return load_data()

@app.post("/api/state")
def update_state(payload: StatePayload):
    data = payload.dict()
    save_data(data)
    return {"status": "success", "message": "Progress synchronized"}

@app.get("/api/gap-analysis")
def gap_analysis():
    data = load_data()
    start_date_str = data.get("start_date", datetime.now().strftime("%Y-%m-%d"))
    pace = int(data.get("pace", 2))
    solved_set = set(data.get("solved", []))
    activity = data.get("activity", {})

    try:
        start_dt = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    except Exception:
        start_dt = date.today()

    today = date.today()
    elapsed_days = (today - start_dt).days
    expected_day_num = max(1, elapsed_days + 1)

    # Determine active days in the last 28 days for dot matrix
    four_weeks_activity = []
    # Start 27 days ago (4 weeks = 28 days total)
    start_matrix_date = today - timedelta(days=27)
    for i in range(28):
        cur_d = start_matrix_date + timedelta(days=i)
        d_str = cur_d.strftime("%Y-%m-%d")
        solved_on_day = activity.get(d_str, [])
        four_weeks_activity.append({
            "date": d_str,
            "day_name": cur_d.strftime("%a"),
            "solved_count": len(solved_on_day),
            "is_today": (cur_d == today),
            "is_active": len(solved_on_day) > 0
        })

    # Gap and Missed Days Detection
    # Calculate last active date
    active_dates = [datetime.strptime(d, "%Y-%m-%d").date() for d, items in activity.items() if len(items) > 0]
    if active_dates:
        last_active = max(active_dates)
        inactive_gap_days = (today - last_active).days
    else:
        last_active = None
        inactive_gap_days = elapsed_days if elapsed_days > 0 else 0

    # Theoretical problem allocation by day
    # Day 1 -> indices [0, pace), Day 2 -> [pace, 2*pace), etc.
    missed_days = []
    current_problem_idx = 0
    day_num = 1
    
    while current_problem_idx < TOTAL_PROBLEMS:
        day_date = start_dt + timedelta(days=day_num - 1)
        day_problems = list(range(current_problem_idx + 1, min(current_problem_idx + pace + 1, TOTAL_PROBLEMS + 1)))
        
        # Check if day is past
        if day_date < today:
            all_done = all(p_id in solved_set for p_id in day_problems)
            if not all_done:
                missed_days.append({
                    "day_num": day_num,
                    "date": day_date.strftime("%Y-%m-%d"),
                    "pending_ids": [p_id for p_id in day_problems if p_id not in solved_set]
                })
        current_problem_idx += pace
        day_num += 1

    # Recovery classification
    if inactive_gap_days >= 4 or len(missed_days) >= 4:
        recovery_status = "long_gap"
        advice = (
            f"Long gap of {inactive_gap_days} days detected. Ebbinghaus forgetting research shows "
            "algorithmic memory decays ~60% after 4 days of inactivity. Do not rush all backlog "
            "problems at once. Execute a 1-problem warmup drill, then recalibrate your roadmap."
        )
    elif len(missed_days) in [1, 2, 3]:
        recovery_status = "minor_miss"
        advice = (
            f"You missed {len(missed_days)} study day(s). Choose either a Sprint Catch-Up (+1 problem/day) "
            f"or shift your timeline forward by {len(missed_days)} day(s) without guilt."
        )
    else:
        recovery_status = "on_track"
        advice = f"You are on track! Today is Day {expected_day_num}. Complete your daily goal to maintain your streak."

    return {
        "expected_day": expected_day_num,
        "inactive_gap_days": inactive_gap_days,
        "missed_days_count": len(missed_days),
        "missed_days": missed_days,
        "recovery_status": recovery_status,
        "advice": advice,
        "matrix_28_days": four_weeks_activity,
        "total_solved": len(solved_set)
    }

@app.post("/api/recalibrate")
def recalibrate_schedule(payload: RecalibratePayload):
    data = load_data()
    today_str = datetime.now().strftime("%Y-%m-%d")

    if payload.mode == "from_today":
        # Recalibrate start date so today becomes the active start point for remaining work
        data["start_date"] = today_str
        save_data(data)
        return {
            "status": "success",
            "message": f"Roadmap successfully recalibrated! Today ({today_str}) is now Day 1 for your remaining topics.",
            "new_start_date": today_str
        }
    elif payload.mode == "shift_days":
        # Shift start date forward by N days
        shift = payload.shift_days or 1
        cur_start = datetime.strptime(data.get("start_date", today_str), "%Y-%m-%d").date()
        new_start = cur_start + timedelta(days=shift)
        new_start_str = new_start.strftime("%Y-%m-%d")
        data["start_date"] = new_start_str
        save_data(data)
        return {
            "status": "success",
            "message": f"Schedule shifted forward by {shift} day(s). New start point: {new_start_str}",
            "new_start_date": new_start_str
        }
    else:
        raise HTTPException(status_code=400, detail="Invalid recalibration mode")

if __name__ == "__main__":
    import uvicorn
    print("Starting Google DSA Tracker FastAPI Backend on http://localhost:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
