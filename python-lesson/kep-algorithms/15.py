n = int(input())
p = 1
for i in range(1, n + 1):
    s = 0
    for j in range(1, i + 1):
        s += j
    p *= s

print(p)

# n = 4
# Tashqi sikl: i = 1, 2, 3, 4
# Ichki sikl: j = 1, 1-2, 1-2-3, 1-2-3-4
# s = 1, 3, 6, 10
# p = 1, 3, 18, 180