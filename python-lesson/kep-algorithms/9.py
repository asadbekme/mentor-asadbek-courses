# 4 xonali sonni topish
# Doskada 4 xonali son yozilgan. Shu sonni teskarisiga o'girib yozishdi. Hosil bo'lgan son berilgan sonning 4 barobariga teng. Toping shu sonni.
# Misollar:
# Input: 2178
# Output: 8712 
def reverse_number(num):
    return int(str(num)[::-1])

def find_four_digit_number():
    for num in range(1000, 10000):
        reversed_num = reverse_number(num)
        if reversed_num == 4 * num:
            return num
    return None

result = find_four_digit_number()
print(result)

# print(reverse_number(2178)) # 8712
# print(str(1234)[::-1]) # 4321