"""
Vasya has a grid with 2 rows and n columns. He colours each cell red, green, or blue.

Vasya is colourblind and can't distinguish green from blue. Determine if Vasya will consider the two rows of the grid to be coloured the same.

Input
The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 100) — the number of columns of the grid.

The following two lines each contain a string consisting of n characters, each of which is either R, G, or B, representing a red, green, or blue cell, respectively — the description of the grid.

Output
For each test case, output "YES" if Vasya considers the grid's two rows to be identical, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

"""

T=int(input())
for _ in range(T):
    n=int(input())
    s1=input()
    s2=input()
    Ans=True
    for i in range(n):
        if s1[i]!=s2[i] and not (s1[i] in "GB" and s2[i] in "GB"):
            Ans=False
            i=n
    if not Ans:
        print("NO")
    else:
        print("YES")
        
""" --- IGNORE ---"""