"""
There are n people in a horizontal line, each looking either to the left or the right. Each person counts the number of people in the direction they are looking. The value of the line is the sum of each person's count.

For example, in the arrangement LRRLL, where L stands for a person looking left and R stands for a person looking right, the counts for each person are [0,3,2,3,4], and the value is 0+3+2+3+4=12.

You are given the initial arrangement of people in the line. For each k from 1 to n, determine the maximum value of the line if you can change the direction of at most k people.

Input
The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 2⋅10^5) — the length of the line.

The following line contains a string consisting of n characters, each of which is either L or R, representing a person facing left or right, respectively — the description of the line.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Please note that the answer for some test cases won't fit into 32-bit integer type, so you should use at least 64-bit integer type in your programming language (like long long for C++).

Output
For each test case, output n space-separated non-negative integers — the maximum value of the line if you can change the direction of at most k people for each k from 1 to n, inclusive.

"""

T=int(input())
for _ in range(T):
    n=int(input())
    if n==1:
        s=input()
        print(0)
        continue
    elif n==2:
        s=input()
        if s=='LR':
            print(1,2)
        elif s=='RL':
            print(2,2)
        elif s=='LL':
            print(2,2)
        else:
            print(2,2)
        continue
    s=input()
    IndL=[]
    IndR=[]
    for i in range(n//2):
        if s[i]=='L':
            IndL.append(i)
    start=n//2
    if n%2==1:
        start+=1
    for i in range(start,n):
        if s[i]=='R':
            IndR.append(n-i-1)
    IndL.sort()
    IndR.sort()
    L1=0
    L2=0
    ans=0
    for i in range(n):
        if s[i]=='L':
            ans+=i
        else:
            ans+=n-i-1
    k=0
    while k<n and (L1<len(IndL) or L2<len(IndR)):
        if L1<len(IndL) and L2<len(IndR):
            if IndL[L1]<=IndR[L2]:
                ans-=IndL[L1]
                ans+=n-IndL[L1]-1
                print(ans,end=' ')
                L1+=1
            else:
                ans-=IndR[L2]
                ans+=n-IndR[L2]-1
                print(ans,end=' ')
                L2+=1
        elif L1<len(IndL):
            ans-=IndL[L1]
            ans+=n-IndL[L1]-1
            print(ans,end=' ')
            L1+=1
        else:
            ans-=IndR[L2]
            ans+=n-IndR[L2]-1
            print(ans,end=' ')
            L2+=1
        k+=1
    while k<n:
        print(ans,end=' ')
        k+=1
        