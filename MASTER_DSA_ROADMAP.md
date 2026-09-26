# Master DSA Roadmap: Google STEP & Microsoft Explore

> **Tracker Tool:** For an interactive daily experience with automatic progress saving, open [`tracker.html`](file:///Users/sumitdas/Desktop/JOB/DSA/tracker.html) in your browser.

---

## Quick Navigation

- [Executive Strategy](#executive-strategy)
- [The 9-Phase Master Syllabus](#the-9-phase-master-syllabus)
  - [Phase 1: Foundations & Time Complexity](#phase-1-foundations--time-complexity)
  - [Phase 2: Arrays & Hashing](#phase-2-arrays-in-place-manipulation--hashing)
  - [Phase 3: Binary Search](#phase-3-binary-search)
  - [Phase 4: Sliding Window & Two Pointers](#phase-4-sliding-window--two-pointers)
  - [Phase 5: Recursion & Backtracking](#phase-5-recursion--backtracking)
  - [Phase 6: Linked Lists & Stacks](#phase-6-linked-lists--stacks)
  - [Phase 7: Binary Trees & BST](#phase-7-binary-trees--binary-search-trees)
  - [Phase 8: Graphs & 2D Matrix Traversals](#phase-8-graphs--2d-matrix-traversals)
  - [Phase 9: 1D Dynamic Programming](#phase-9-1d-dynamic-programming)
- [Google STEP Top 10 Checklist](#google-step-top-10-strike-list)
- [Microsoft Explore Top 10 Checklist](#microsoft-explore-top-10-strike-list)
- [15 Core Patterns Reference](#15-core-patterns-reference)
- [Python Interview Reference](#python-interview-reference)

---

## Executive Strategy

1. **Master Archetypes, Not 2,000 Questions:** 95% of Big Tech 2nd-year interview questions come from **7 core algorithmic patterns**.
2. **The 25-Minute Rule:** If stuck for more than 20 minutes, watch the video in your PDF sheet. Understand the logic, close YouTube, and code it from scratch in Python.
3. **Google Doc Protocol:** Google STEP interviews are held in a plain **Google Doc** without syntax highlighting, auto-complete, or code execution. Practice writing code in a blank text file.

---

## The 9-Phase Master Syllabus

<details open>
<summary><h3>Phase 1: Foundations & Time Complexity</h3></summary>

| Step | Topic / Problem | PDF Ref | Key Concept |
|:---:|:---|:---:|:---|
| 01 | **Time & Space Complexity Theory** | Sec 1.1 | $O(1) < O(\log N) < O(N) < O(N \log N) < O(N^2)$ |
| 02 | **Complexity of Python Operations** | Sec 1.1 | `list.pop(0)` is $O(N)$ vs `deque.popleft()` is $O(1)$ |
| 03 | **How to Store Frequency & Hashing** | Sec 1.4 | `dict` & `Counter` lookups in $O(1)$ time |

</details>

<details open>
<summary><h3>Phase 2: Arrays, In-Place Manipulation & Hashing</h3></summary>

| Step | Problem | LeetCode | Difficulty | Target Company | Pattern |
|:---:|:---|:---:|:---:|:---:|:---|
| 04 | Largest Element in an Array | [GFG](https://www.geeksforgeeks.org/problems/largest-element-in-array/1) | Easy | Any | Single pass scan |
| 05 | Second Largest Element | [GFG](https://www.geeksforgeeks.org/problems/second-largest3735/1) | Easy | Any | Track largest & 2nd largest |
| 06 | Remove Duplicates from Sorted Array | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | Microsoft | In-place two pointers |
| 07 | Move Zeroes | [LC 283](https://leetcode.com/problems/move-zeroes/) | Easy | Any | In-place partition |
| 08 | Missing Number | [LC 268](https://leetcode.com/problems/missing-number/) | Easy | Any | XOR / Sum formula |
| 09 | Max Consecutive Ones | [LC 485](https://leetcode.com/problems/max-consecutive-ones/) | Easy | Any | Rolling counter |
| 10 | **Two Sum** | [LC 1](https://leetcode.com/problems/two-sum/) | Easy | Google & MS | Hash map complement |
| 11 | **Maximum Subarray (Kadane's)** | [LC 53](https://leetcode.com/problems/maximum-subarray/) | Medium | Microsoft | `max(num, curr + num)` |
| 12 | **Best Time to Buy & Sell Stock** | [LC 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Any | Track running minimum |
| 13 | **Longest Consecutive Sequence** | [LC 128](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Google | Set lookup `(num - 1) not in s` |
| 14 | **Rotate Matrix by 90°** | [LC 48](https://leetcode.com/problems/rotate-image/) | Medium | Microsoft | Transpose + Reverse rows |
| 15 | **3Sum** | [LC 15](https://leetcode.com/problems/3sum/) | Medium | Google & MS | Sort + Two Pointers |

</details>

<details open>
<summary><h3>Phase 3: Binary Search</h3></summary>

| Step | Problem | LeetCode | Difficulty | Target Company | Pattern |
|:---:|:---|:---:|:---:|:---:|:---|
| 16 | Binary Search | [LC 704](https://leetcode.com/problems/binary-search/) | Easy | Foundation | Standard template |
| 17 | Search Insert Position | [LC 35](https://leetcode.com/problems/search-insert-position/) | Easy | Any | Lower bound check |
| 18 | Floor / Ceil in Sorted Array | [GFG](https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1) | Easy | Any | Boundary tracking |
| 19 | First & Last Position of Element | [LC 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | Any | Double binary search |
| 20 | **Search in Rotated Sorted Array** | [LC 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Google & MS | Identify sorted half |
| 21 | Find Min in Rotated Sorted Array | [LC 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Any | Inflection point binary search |
| 22 | **Koko Eating Bananas** | [LC 875](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Google | Binary search on answer space |

</details>

<details open>
<summary><h3>Phase 4: Sliding Window & Two Pointers</h3></summary>

| Step | Problem | LeetCode | Difficulty | Target Company | Pattern |
|:---:|:---|:---:|:---:|:---:|:---|
| 23 | **Longest Substring Without Repeating** | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Google Top | Last-seen hash map |
| 24 | **Max Consecutive Ones III** | [LC 1004](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | Google | Variable window with $\le K$ zeroes |
| 25 | **Fruit Into Baskets** | [LC 904](https://leetcode.com/problems/fruit-into-baskets/) | Medium | Google | Window with $\le 2$ keys |
| 26 | Max Points From Cards | [LC 1423](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Medium | Any | Total sum minus min subarray |
| 27 | **Subarray Sum Equals K** | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Google | Prefix sum frequency map |

</details>

<details open>
<summary><h3>Phase 5: Recursion & Backtracking</h3></summary>

| Step | Problem | LeetCode | Difficulty | Target Company | Pattern |
|:---:|:---|:---:|:---:|:---:|:---|
| 28 | Recursion Intro & Fibonacci | [LC 509](https://leetcode.com/problems/fibonacci-number/) | Easy | Foundation | Base case + subproblems |
| 29 | **Subsets / Power Set** | [LC 78](https://leetcode.com/problems/subsets/) | Medium | Google | Pick vs. Don't Pick tree |
| 30 | **Generate Parentheses** | [LC 22](https://leetcode.com/problems/generate-parentheses/) | Medium | Google | Pruning invalid branches |
| 31 | **Combination Sum** | [LC 39](https://leetcode.com/problems/combination-sum/) | Medium | Google | Reusable element decision tree |
| 32 | Phone Letter Combinations | [LC 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | Any | String recursion mapping |

</details>

<details open>
<summary><h3>Phase 6: Linked Lists & Stacks</h3></summary>

| Step | Problem | LeetCode | Difficulty | Target Company | Pattern |
|:---:|:---|:---:|:---:|:---:|:---|
| 33 | Middle of Linked List | [LC 876](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | Microsoft | Slow/Fast pointers |
| 34 | **Reverse Linked List** | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | Easy | Microsoft Top | Iterative 3-pointer swap |
| 35 | **Detect Loop in Linked List** | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | Easy | Microsoft | Floyd's cycle algorithm |
| 36 | **Starting Point of Loop** | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | Microsoft | Cycle entry math |
| 37 | **Remove Nth Node From End** | [LC 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Microsoft | Fast pointer $N$-step lead |
| 38 | Understand Deque in Python | Theory | - | - | `collections.deque` |
| 39 | **Valid Parentheses** | [LC 20](https://leetcode.com/problems/valid-parentheses/) | Easy | Microsoft | LIFO Stack match |
| 40 | **Min Stack** | [LC 155](https://leetcode.com/problems/min-stack/) | Medium | Microsoft | Stack of pairs `(val, min)` |
| 41 | Next Greater Element I | [LC 496](https://leetcode.com/problems/next-greater-element-i/) | Easy | Any | Monotonic decreasing stack |

</details>

<details open>
<summary><h3>Phase 7: Binary Trees & Binary Search Trees</h3></summary>

| Step | Problem | LeetCode | Difficulty | Target Company | Pattern |
|:---:|:---|:---:|:---:|:---:|:---|
| 42 | Preorder, Inorder, Postorder | Theory | - | Foundation | DFS tree traversals |
| 43 | **Level Order Traversal** | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | Google & MS | BFS queue level-by-level |
| 44 | Height / Max Depth of Tree | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Any | `1 + max(left, right)` |
| 45 | **Diameter of Binary Tree** | [LC 543](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | Google | Update diameter at each node |
| 46 | Right Side View of Tree | [LC 199](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | Any | Level order / right-first DFS |
| 47 | **Validate Binary Search Tree** | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | Microsoft | Range bounds `low < val < high` |
| 48 | **Lowest Common Ancestor (LCA)** | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | Google | Tree recursion backpropagation |

</details>

<details open>
<summary><h3>Phase 8: Graphs & 2D Matrix Traversals</h3></summary>

| Step | Problem | LeetCode | Difficulty | Target Company | Pattern |
|:---:|:---|:---:|:---:|:---:|:---|
| 49 | Graph Representation | Theory | - | Foundation | `adj = defaultdict(list)` |
| 50 | BFS & DFS of Graph | Theory | - | Foundation | Queue vs Recursion |
| 51 | **Number of Islands** | [LC 200](https://leetcode.com/problems/number-of-islands/) | Medium | Google Top | 4-directional matrix BFS/DFS |
| 52 | **Rotting Oranges** | [LC 994](https://leetcode.com/problems/rotting-oranges/) | Medium | Any | Multi-source BFS |
| 53 | Flood Fill | [LC 733](https://leetcode.com/problems/flood-fill/) | Easy | Any | Connected component fill |
| 54 | **Course Schedule I** | [LC 207](https://leetcode.com/problems/course-schedule/) | Medium | Google | Topo Sort / Kahn's cycle check |

</details>

<details open>
<summary><h3>Phase 9: 1D Dynamic Programming</h3></summary>

| Step | Problem | LeetCode | Difficulty | Target Company | Pattern |
|:---:|:---|:---:|:---:|:---:|:---|
| 55 | DP Introduction (Memoization) | Theory | - | Foundation | Cache overlapping subproblems |
| 56 | **Climbing Stairs** | [LC 70](https://leetcode.com/problems/climbing-stairs/) | Easy | Microsoft | `dp[i] = dp[i-1] + dp[i-2]` |
| 57 | **House Robber** | [LC 198](https://leetcode.com/problems/house-robber/) | Medium | Google & MS | `max(dp[i-1], dp[i-2] + nums[i])` |
| 58 | **Grid Unique Paths** | [LC 62](https://leetcode.com/problems/unique-paths/) | Medium | Any | 2D Grid DP `dp[r][c]` |

</details>

---

## Google STEP Top 10 Strike List

1. [LC 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Sliding Window)
2. [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) (Grid BFS/DFS)
3. [LC 560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Prefix Map)
4. [LC 236: Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) (Tree Backtracking)
5. [LC 33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Modified Binary Search)
6. [LC 904: Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) (Sliding Window)
7. [LC 994: Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (Multi-source BFS)
8. [LC 15: 3Sum](https://leetcode.com/problems/3sum/) (Two Pointers)
9. [LC 39: Combination Sum](https://leetcode.com/problems/combination-sum/) (Backtracking)
10. [LC 875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (Binary Search on Answer)

---

## Microsoft Explore Top 10 Strike List

1. [LC 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Pointer Swap)
2. [LC 141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Fast & Slow Pointers)
3. [LC 142: Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Cycle Entry Math)
4. [LC 19: Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Two Pointer Lead)
5. [LC 98: Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (Range Bounds)
6. [LC 48: Rotate Image](https://leetcode.com/problems/rotate-image/) (Matrix Transpose)
7. [LC 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (LIFO Stack)
8. [LC 155: Min Stack](https://leetcode.com/problems/min-stack/) (Data Structure Design)
9. [LC 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Kadane's Algorithm)
10. [LC 70: Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (1D DP)

---

## 15 Core Patterns Reference

```
01. Sliding Window         - Subarray/substr with max/min/sum/frequency bounds
02. Two Pointers           - Sorted arrays, pair-sums, in-place partitions
03. Fast & Slow Pointers   - Cycle detection, finding middle of linked list
04. Binary Search          - Sorted arrays, boundaries, answer space
05. Prefix Sum             - Range sum queries, subarray sum equals K
06. Greedy Algorithms      - Local-optimal choice leads to global-optimal
07. Backtracking           - Permutations, combinations, subsets, pruning
08. 1D Dynamic Programming - Linear subproblems (Climbing stairs, House robber)
09. 2D / Grid DP           - Grid navigation paths, matrix path computation
10. Bit Manipulation       - XOR tricks (A ^ A = 0), masks, subsets via bits
11. Hashing & Frequency    - O(1) lookups, anagrams, grouping
12. Graphs - BFS/DFS       - Connected components, flood fill, shortest path
13. Topological Sort       - Dependency resolution, DAG scheduling (Course Schedule)
14. Trees - DFS Patterns   - LCA, traversals, path sum, subtree validation
15. Heaps & Priority Queue - Top-K elements, k-way merges, task scheduling
```

---

## Python Interview Reference

```python
# Collections
from collections import Counter, defaultdict, deque
freq = Counter("google")                    # Frequency count in O(N)
graph = defaultdict(list)                   # Adjacency list without KeyError
queue = deque([root])                       # O(1) popleft() for BFS

# Heaps
import heapq
min_heap = []
heapq.heappush(min_heap, val)               # O(log N)
min_val = heapq.heappop(min_heap)           # O(log N)

# Binary Search
import bisect
idx = bisect.bisect_left(arr, target)       # First insertion index in sorted array
```
