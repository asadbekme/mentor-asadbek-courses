# Tublikga tekshirish
# Agar son tub bo'lsa, Yes aks holda No chiqaring

n = int(input())
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

print("Yes" if is_prime else "No")

# break va flag'siz yechim
# def is_prime(n):
#     if n <= 1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False    # bo'luvchi topildi → tub emas
    
#     return True             # bo'luvchi topilmadi → tub


# n = int(input())
# print("Yes" if is_prime(n) else "No")