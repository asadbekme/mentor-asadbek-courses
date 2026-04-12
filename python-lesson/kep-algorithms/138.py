# Sizga satr(string) berilgan. Ushbu satr butun son ekanligini tekshiring. 
# Agar satr butun son bo'lsa, Yes qaytaring, aks holda No qaytaring.
# Misollar:
# Input: "123"
# Output: Yes
# Input: "12r1"
# Output: No
# Input: "-5"
# Output: Yes
# Input: "1.0"
# Output: No
s = input()
def is_integer_string(s):
    # Satrdagi har bir belgini tekshirish
    for char in s:
        if char not in "0123456789-":
            return "No"
    
    # Agar satr boshida '-' bo'lsa, uni olib tashlash
    if s.startswith('-'):
        s = s[1:]
    
    # Qolgan qism faqat raqamlardan iborat bo'lishi kerak
    if s.isdigit():
        return "Yes"
    
    return "No"

print(is_integer_string(s))