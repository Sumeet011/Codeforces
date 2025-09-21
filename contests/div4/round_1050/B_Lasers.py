"""B. Lasers
Time Limit: 2 seconds
Memory Limit: 256 megabytes

There is a 2D-coordinate plane that ranges from (0,0) to (x,y). You are located at (0,0) and want to head to (x,y).
However, there are n horizontal lasers, with the i-th laser continuously spanning (0,ai) to (x,ai). Additionally, there are m vertical lasers, with the i-th laser continuously spanning (bi,0) to (bi,y).

You may move in any direction to reach (x,y), but your movement must be a continuous curve that lies inside the plane. Every time you cross a vertical or a horizontal laser, it counts as one crossing. Particularly, if you pass through an intersection point between two lasers, it counts as two crossings.

For example, if x = y = 2, n = m = 1, a = [1], b = [1], the movement can be as follows:

Your task is to find the minimum number of crossings necessary to reach (x,y).

Input:
- The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.
- The first line of each test case contains four integers n, m, x, y (1 ≤ n, m ≤ 2·10^5, 2 ≤ x, y ≤ 10^9).
- The following line contains n integers a1, a2, ..., an (0 < ai < y) — the y-coordinates of the horizontal lasers. It is guaranteed that ai > ai−1 for all i > 1.
- The following line contains m integers b1, b2, ..., bm (0 < bi < x) — the x-coordinates of the vertical lasers. It is guaranteed that bi > bi−1 for all i > 1.

It is guaranteed that the sum of n and m over all test cases does not exceed 2·10^5.

Output:
For each test case, output the minimum number of crossings necessary to reach (x,y).
"""

T = int(input())
for _ in range(T):
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # For now, we just print n+m (placeholder)
    # Later you can implement the correct min crossings logic
    print(n + m)
