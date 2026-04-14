import math

n = int(input())

m = int(math.isqrt(n))   # floor(√n)
total = 0

# k = 1 dan m-1 gacha: har birida 2k+1 ta son bor
for k in range(1, m):
    total += k * (2 * k + 1)

# k = m uchun: m² dan n gacha → (n - m² + 1) ta son
total += m * (n - m * m + 1)

print(total)