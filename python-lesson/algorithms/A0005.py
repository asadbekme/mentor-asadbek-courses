N = int(input())
A, B, C = map(int, input().split())

print("Yes" if A + B + C >= N else "No")


# comment
"""
**Test:**

Input:        Input:
1000          1000
300 400 200   200 300 100

300+400+200   200+300+100
= 900 < 1000  = 600 < 1000

Output: No    Output: No

Input:
500
200 200 200

200+200+200 = 600 >= 500
Output: Yes ✅
"""