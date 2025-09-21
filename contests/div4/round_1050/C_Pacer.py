"""
The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20-meter pacer test will begin in 30 seconds. Line up at the start. A single lap should be completed every time you hear this sound. Ding! Remember to run in a straight line and run as long as possible. The test will begin on the word "start." On your mark. Get ready!...

Farmer John is running the FitnessGram Pacer Test! Farmer John takes one minute to run to the other side of the gym. Therefore, at the start of each minute, FJ can choose to either run to the other side of the gym or stay in place. If he chooses to run to the other side of the gym, he gains one point.

FJ will run the Pacer Test until the start of the m-th minute. Initially (at the start of the 0-th minute), FJ is at the starting side of the gym, which we will denote as side 0. The opposite side of the gym is denoted side 1.

The pacer test audio plays n times. At the start of the a_i-th minute, FJ must be at the b_i-th side of the gym.

Your task is to determine the maximum number of points FJ can acquire while ensuring that he meets the audio's requirements.

Input:
- The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.
- The first line of each test case contains two integers n and m (1 ≤ n ≤ 2·10^5, n ≤ m ≤ 10^9) — the number of requirements and the total number of minutes.
- The following n lines each contain two integers a_i and b_i (1 ≤ a_i ≤ m, b_i ∈ {0,1}) — the i-th requirement by the audio. It is guaranteed that a_i > a_{i-1} for all i > 1.

It is guaranteed that the sum of n over all test cases does not exceed 2·10^5.

Output:
For each test case, output the maximum number of points that FJ can acquire.
"""
n = int(input())
 
for _ in range(n):
    n,m = [int(i) for i in input().split()]
    ans = m
    x = 0
    y = 0
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        if (a-x)%2!=abs(y-b):
            ans-=1
        x = a
        y = b
    print(ans)
