# math modul
# import math
# ceil bu sonni yuqoriga qarab yaxlitlaydi
# floor bu sonni pastga qarab yaxlitlaydi
# round bu sonni eng yaqin butun songa yaxlitlaydi
# print(math.ceil(3.2))  # 4
# print(math.floor(3.8))  # 3
# print(round(3.5))  # 4

# * 1-usul:
# import math

# a, b, c = map(int, input().split())

# print(math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2))

# * 2-usul:
a, b, c = map(int, input().split())

def partalar(n):
    return n // 2 if n % 2 == 0 else n // 2 + 1

print(partalar(a) + partalar(b) + partalar(c))

"""
**Test:**
20 21 22  →  10 + 11 + 11 = 32  ✅
16 18 20  →   8 +  9 + 10 = 27  ✅
 1  1  1  →   1 +  1 +  1 =  3  ✅
"""
