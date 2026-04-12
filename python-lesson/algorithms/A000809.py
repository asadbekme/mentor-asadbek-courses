N, K = map(int, input().split())
print(K // N)
print(K - (N * (K // N)))
"""
Input: 3 14  →  14 // 3 = 4  ✅
Input: 5 25  →  25 // 5 = 5  ✅
Input: 4 14  →  14 // 4 = 3  ✅
"""