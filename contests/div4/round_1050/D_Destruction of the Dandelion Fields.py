"""Farmer John has a lawnmower, initially turned off. He also has n fields, with the i-th field having a_i dandelions. He will visit all the fields in any order he wants, and each field exactly once.

FJ's lawnmower seems to have a mind of its own. Right before visiting a field, it checks if the field has an even or odd number of dandelions. If it has an odd number, then the lawnmower toggles its state (if it is off, it turns on; if it is on, it turns off). Then, if the lawnmower is on, it will cut all dandelions in that field. Otherwise, if the lawnmower is off, then FJ will simply visit the field and cut no dandelions.

If FJ visits the n fields in optimal order, what is the maximum total number of dandelions he can cut?

Input:
- The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.
- The first line of each test case contains an integer n (1 ≤ n ≤ 2·10^5) — the number of fields.
- The following line contains n space-separated integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) — the number of dandelions in each field.

It is guaranteed that the sum of n over all test cases does not exceed 2·10^5.

Output:
For each test case, output an integer on a new line: the maximum number of dandelions FJ can cut if he visits all n fields in optimal order.
"""

T=int(input())
for _ in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    ans=0
    C=0
    Have=False
    for A in a:
        if A%2!=0:
            C+=1
            Have=True
    if C%2==0:
        C=C/2
    else:
        C=(C+1)/2
    i=0
    while i<n and C>0:
        if a[i]%2==1:
            C-=1
            ans+=a[i]
        i+=1
    i=0
    if Have:
        while i<n:
            if a[i]%2==0:
                ans+=a[i]
            i+=1
    print(ans)