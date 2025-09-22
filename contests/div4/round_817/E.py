"""
You have n rectangles, the i-th rectangle has height hi and width wi.

You are asked q queries of the form hs ws hb wb.

For each query output the total area of rectangles you own that can fit a rectangle of height hs and width ws while also fitting in a rectangle of height hb and width wb. 
In other words, print ∑hi⋅wi for i such that hs < hi < hb and ws < wi < wb.

Please note, that if two rectangles have the same height or the same width, then they cannot fit inside each other. Also note that you cannot rotate rectangles.

Please note that the answer for some test cases won't fit into 32-bit integer type, so you should use at least 64-bit integer type in your programming language (like long long for C++).

Input
The first line of the input contains an integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains two integers n and q (1 ≤ n ≤ 10^5; 1 ≤ q ≤ 10^5) — the number of rectangles you own and the number of queries.

Then n lines follow, each containing two integers hi and wi (1 ≤ hi, wi ≤ 1000) — the height and width of the i-th rectangle.

Then q lines follow, each containing four integers hs, ws, hb, wb (1 ≤ hs < hb, ws < wb ≤ 1000) — the description of each query.

The sum of q over all test cases does not exceed 10^5, and the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output q lines, the i-th line containing the answer to the i-th query.

"""