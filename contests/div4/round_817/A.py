"""A. Spell Check
time limit per test: 1 second
memory limit per test: 256 megabytes

Timur likes his name. As a spelling of his name, he allows any permutation of the letters of the name.
For example, the following strings are valid spellings of his name:
Timur, miurT, Trumi, mriTu.

Note: The correct spelling must have an uppercase 'T' and lowercase letters for the rest.

Today he wrote a string s of length n consisting only of uppercase or lowercase Latin letters.
He asks you to check if s is the correct spelling of his name.

Input
The first line of the input contains an integer t (1 ≤ t ≤ 10^3) — the number of test cases.

The first line of each test case contains an integer n (1 ≤ n ≤ 10) — the length of string s.

The second line of each test case contains a string s consisting of only uppercase or lowercase Latin characters.

Output
For each test case, output "YES" (without quotes) if s satisfies the condition, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
"""
T=int(input())
for _ in range(T):
    n=int(input())
    s=input()
    if n==5 and sorted(s)==sorted("Timur"):
        print("YES")
    else:
        print("NO")