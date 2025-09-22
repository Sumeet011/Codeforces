"""
F. L-shapes
time limit per test: 1 second
memory limit per test: 256 megabytes

An L-shape is a figure on gridded paper that looks like the first four pictures below. 
An L-shape contains exactly three shaded cells (denoted by *), which can be rotated in any way.

You are given a rectangular grid. Determine if it contains L-shapes only, where L-shapes can't touch an edge or corner. More formally:

- Each shaded cell in the grid is part of exactly one L-shape, and
- No two L-shapes are adjacent by edge or corner.

For example, the last two grids in the picture above do not satisfy the condition because the two L-shapes touch by corner and edge, respectively.

Input
The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n and m (1 ≤ n, m ≤ 50) — the number of rows and columns in the grid, respectively.

Then n lines follow, each containing m characters. Each of these characters is either '.' or '*' — an empty cell or a shaded cell, respectively.

Output
For each test case, output "YES" if the grid is made up of L-shapes that don't share edges or corners, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

"""
def check_corners(r, c):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 0 <= r + dx < n and 0 <= c + dy < m and grid[r + dx][c + dy] == '*' and visited[r + dx][c + dy] != \
                    visited[r][c]:
                return False
    return True
 
 
for _ in range(int(input())):
    n, m = map(int, input().split())
    grid, visited, idx, s, valid = [input() for _ in range(n)], [[0] * m for _ in range(n)], 1, set(), True
 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue
            elif visited[i][j]:
                if not check_corners(i, j):
                    valid = False
                    break
                else:
                    continue
 
            shapes = 0
 
            if j + 1 < m and i + 1 < n and grid[i][j + 1] == '*' and grid[i + 1][j + 1] == '*':
                visited[i][j] = idx
                visited[i][j + 1] = idx
                visited[i + 1][j + 1] = idx
                shapes += 1
 
            if i + 1 < n and j + 1 < m and grid[i][j + 1] == '*' and grid[i + 1][j] == '*':
                visited[i][j] = idx
                visited[i][j + 1] = idx
                visited[i + 1][j] = idx
                shapes += 1
 
            if i + 1 < n and j + 1 < m and grid[i + 1][j] == '*' and grid[i + 1][j + 1] == '*':
                visited[i][j] = idx
                visited[i + 1][j + 1] = idx
                visited[i + 1][j] = idx
                shapes += 1
 
            if j - 1 >= 0 and i + 1 < n and grid[i + 1][j] == '*' and grid[i + 1][j - 1] == '*':
                visited[i][j] = idx
                visited[i + 1][j] = idx
                visited[i + 1][j - 1] = idx
                shapes += 1
 
            if shapes != 1:
                valid = False
                break
 
            s.add(idx)
            idx += 1
 
    if valid:
        print('YES')
    else:
        print('NO')  