lst = list(map(int, input().split()))

for num in lst:
    if num == 127:
        break                  # 127 ga yetdik — to'xtaymiz

    if num % 2 != 0:           # toq son
        print(num)


# lst = [1, 3, 127, 5, 7, 9]

# num=1:   127 emas → toq ✅ → print(1)
# num=3:   127 emas → toq ✅ → print(3)
# num=127: 127 ✅  → break! (5,7,9 ga qaramaymiz)

# Output:
# 1
# 3