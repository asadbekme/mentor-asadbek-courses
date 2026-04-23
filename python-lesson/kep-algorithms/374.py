n = int(input())
a = list(map(int, input().split()))

# min = a[0]
# min_index = 0
# for i in range(1, n):
#    if a[i] < min:
#       min = a[i]
#       min_index = i

# print(min_index + 1)

min_value = min(a)
min_index = a.index(min_value)
print(min_index + 1)