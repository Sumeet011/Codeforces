"""Farmer John has n arrays a_1, a_2, ..., a_n that may have different lengths. He will stack the arrays on top of each other, resulting in a grid with n rows. The arrays are left-aligned and can be stacked in any order he desires.

Then, gravity will take place. Any cell that is not on the bottom row and does not have an element beneath it will fall down a row. This process will be repeated until there are no cells that satisfy the aforementioned constraint.

Over all possible ways FJ can stack the arrays, output the lexicographically minimum bottom row after gravity takes place.

Input:
- The first line contains t (1 ≤ t ≤ 1000) — the number of test cases.
- The first line of each test case contains n (1 ≤ n ≤ 2·10^5) — the number of arrays.
- The following n lines describe each array:
    - The first integer k_i (1 ≤ k_i ≤ 2·10^5) denotes the length of a_i.
    - Then, k_i space-separated integers a_{i1}, a_{i2}, ..., a_{ik_i} follow (1 ≤ a_{ij} ≤ 2·10^5).

It is guaranteed that the sum of n and the sum of all k_i over all test cases does not exceed 2·10^5.

Output:
For each test case, output the lexicographically minimum bottom row after gravity takes place.
"""
T = int(input())
for _ in range(T):
    n = int(input())
    arrays = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        # The first number is the length, remove it
        k = arr[0]
        arrays.append(arr[1:])
    
    # Sort arrays lexicographically
    arrays.sort()
    
    i=0
    ans=[]
    
    for col in arrays:
        while i<len(col):
            ans.append(col[i])
            i+=1
    
    for a in ans:
        print(a, end=' ')
