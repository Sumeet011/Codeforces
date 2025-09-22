"""
Three guys play a game: first, each person writes down n distinct words of length 3. 
Then, they total up the number of points as follows:

- If a word was written by one person — that person gets 3 points.
- If a word was written by two people — each of the two gets 1 point.
- If a word was written by all three — nobody gets any points.

In the end, how many points does each player have?

Input
The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 1000) — the number of words written by each person.

The following three lines each contain n distinct strings — the words written by each person. Each string consists of 3 lowercase English characters.

Output
For each test case, output three space-separated integers — the number of points each of the three guys earned. 
You should output the answers in the same order as the input; the i-th integer should be the number of points earned by the i-th guy.

"""

T=int(input())
for _ in range(T):
    n=int(input())
    Map={}
    for i in range(3):
        words=input().split()
        for word in words:
            if word in Map and Map[word][:-1]!=i:
                Map[word].append(i)
            else:
                Map[word]=[i]
    ans=[0,0,0]
    for key in Map:
        if len(Map[key])==1:
            ans[Map[key][0]]+=3
        elif len(Map[key])==2:
            ans[Map[key][0]]+=1
            ans[Map[key][1]]+=1
    print(*ans)
    