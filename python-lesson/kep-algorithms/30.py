n = int(input())
a = list(map(int, input().split()))

# 1-qatnashgan 1 ni o'rnini, 2-qatnashgan 2 ni o'rnini, 3-qatnashgan 3 ni o'rnini topish kerak. Agar qatnashmagan bo'lsa, -1 ni chiqaring.
count1 = 0
count2 = 0
count3 = 0

res1 = -1
res2 = -1
res3 = -1

for i in range(n):
    if a[i] == 1:
        count1 += 1
        if count1 == 1:
            res1 = i + 1
    elif a[i] == 2:
        count2 += 1
        if count2 == 2:
            res2 = i + 1
    elif a[i] == 3:
        count3 += 1
        if count3 == 3:
            res3 = i + 1

print(res1, res2, res3)

# Example:
# Input:
# n = 4
# a = [2, 1, 2, 3]

# i=0: a[0]=2 → count2=1 (2-chi emas, o'tkazib yuboramiz)
# i=1: a[1]=1 → count1=1 → res1 = 2  ✅
# i=2: a[2]=2 → count2=2 → res2 = 3  ✅
# i=3: a[3]=3 → count3=1 (3-chi emas, o'tkazib yuboramiz)

# res3 hali -1 bo'lib qoldi

# Output: 2 3 -1  ✅