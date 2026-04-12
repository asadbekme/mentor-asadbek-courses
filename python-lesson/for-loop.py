students = ["Alice", "Bob", "Charlie", "David", "Eve"]
for student in students:    
    print(student)

# 1-iteratsiya student = "Alice"
# 2-iteratsiya student = "Bob"
# 3-iteratsiya student = "Charlie"
# 4-iteratsiya student = "David"    
# 5-iteratsiya student = "Eve"

for guest in students:
    print(f"Hurmatli {guest}, sizni interviewga taklif qilmoqchiman.")
    print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi.")

# Sonlar ro'yxati uchun for loop
even_numbers = list(range(2, 51, 2)) # 2 dan 50 gacha bo'lgan juft sonlar ro'yxati
for number in even_numbers:
    print(number)

print("Dastur tugadi.")

# 1 ning kvadrati 1 ga teng.
# 2 ning kvadrati 4 ga teng.
# 3 ning kvadrati 9 ga teng. 
sonlar = list(range(1, 11)) # 1 dan 10 gacha bo'lgan sonlar ro'yxati
for son in sonlar:
    print(f"{son} ning kvadrati {son ** 2} ga teng.")

people = ["Alice", "Bob", "Charlie", "David", "Eve"]
for person in people:
    print(person)

# 2-usul: range() funksiyasi yordamida indekslar orqali iteratsiya qilish
for index in range(len(people)):
    print(index)
    print(people[index])

print("Dastur tugadi.")

# 1-iteratsiya index = 0, people[index] = "Alice"
# 2-iteratsiya index = 1, people[index] = "Bob"
# 3-iteratsiya index = 2, people[index] = "Charlie"
# 4-iteratsiya index = 3, people[index] = "David"
# 5-iteratsiya index = 4, people[index] = "Eve"

# 1 dan 100 gacha bo'lgan sonlarni chiqarish
sonlar = list(range(1, 101)) # 1 dan 100 gacha bo'lgan sonlar ro'yxati
for son in sonlar:
    print(son)

for son in range(1, 101):
    print(son)