# print(10 / 3) # 3.3333333333333335
# print(10 // 3) # 3
# print(10 % 3) # 1
# print("5" + "3") # '53'
# print("5" * 3) # '555'

# module - bu kodlar to'plami bo'lib, ularni boshqa fayllarda ishlatish mumkin. 
# Masalan, calculate.py faylida matematik amallarni bajaruvchi funksiyalar mavjud. 
# Biz bu funksiyalarni test.py faylida import qilib ishlatamiz.  
import calculate

print(calculate.add(5, 3)) # 8
print(calculate.subtract(5, 3)) # 2
print(calculate.multiply(5, 3)) # 15
print(calculate.divide(5, 3)) # 1.6666666666666667
print(calculate.power(5, 3)) # 125
print(calculate.square_root(25)) # 5.0
print(calculate.square(5)) # 25

# print(4 ** 0.5) # 2.0
print("2" not in "0123456789-") # False
print("-" not in "0123456789-") # False


