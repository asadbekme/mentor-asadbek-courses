# =====================================================
# Minimum va Maksimum to'rt sonning yig'indisi
# =====================================================

nums = list(map(int, input().split()))   # 5 ta son

total = sum(nums)

min_sum = total - max(nums)   # eng kattasini chiqarib tashlash
max_sum = total - min(nums)   # eng kichigini chiqarib tashlash

print(min_sum, max_sum)


# **Test:**
# Input:  1 2 3 4 5
# total = 15
# min_sum = 15 - 5 = 10
# max_sum = 15 - 1 = 14
# Output: 10 14  ✅