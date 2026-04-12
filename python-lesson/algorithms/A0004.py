# g'oya: 2 * sum(set) - sum(array) = yolg'iz son
# 2*(1+2+3+4) - (1+2+3+4+3+2+1)
# 2*10 - 16 = 4 ✅

n = int(input())
nums = list(map(int, input().split()))

result = 2 * sum(set(nums)) - sum(nums)
print(result)

# [1, 2, 3, 4, 3, 2, 1]
# set → {1, 2, 3, 4}

# 2 × (1+2+3+4) = 20
#     (1+2+3+4+3+2+1) = 16
# 20 - 16 = 4 ✅