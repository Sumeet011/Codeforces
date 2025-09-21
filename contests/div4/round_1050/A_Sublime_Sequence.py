""" Time Limit: 1 second
Memory Limit: 256 megabytes

Farmer John has an integer x. He creates a sequence of length n by alternating integers x and -x, starting with x.
For example, if n = 5, the sequence looks like:
x, -x, x, -x, x

He asks you to find the sum of all integers in the sequence.

Input:
- The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases.
- Each of the next t lines contains two integers x and n (1 ≤ x, n ≤ 10).

Output:
For each test case, output the sum of all integers in the sequence.

Example:

Input:
4
1 4
2 5
3 6
4 7

Output:
0
2
0
4
"""

T=int(input())
for _ in range(T):
    x,n=map(int,input().split())
    if n%2==0:
        print(0)
    else:
        print(x)
