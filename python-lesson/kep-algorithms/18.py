# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

# Antiqa ketma-ketlik: 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 9, 9, 9, 10, ..., n 
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
