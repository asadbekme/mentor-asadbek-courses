text = "test"
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3]) 
# print(text[-1]) # t

# 1-usul:
# for char in text:
#     print(char)

# 2-usul:
# for i in range(len(text)):
#     print(text[i])

# Algoritm
# N = input().strip()

# odd_sum = 0   # toq o'rindagi raqamlar yig'indisi (1,3,5-chi pozitsiyalar)
# even_sum = 0  # juft o'rindagi raqamlar yig'indisi (2,4,6-chi pozitsiyalar)

# for i in range(len(N)):
#     digit = int(N[i])
#     if (i + 1) % 2 == 1:        # odd position (1-based)
#         odd_sum += digit
#     else:
#         even_sum += digit

# diff = odd_sum - even_sum

# print("Yes") if diff == 0 or diff % 11 == 0 else print("No")

print(list(" Yes.  ".strip())) # ['Y', 'e', 's', '.']
print("No ".strip()) # 'No'
