# Time limit exceeded
# n = 10 ** 9
# n = int(input())
# count = 0
# for num in range(1, n + 1):
#     if num % 12 == 0 or num % 5 == 0:
#         count += 1

# print(count)

# O(1) yechim
n = int(input())
count = n // 12 + n // 5 - n // 60   # 12 va 5 ning eng kichik umumiy ko'paytmasi 60
print(count)