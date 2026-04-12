year = int(input())

# Kabisa yilini tekshirish
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# 255-kun (yanvar=0 dan boshlab)
day = 12 if is_leap else 13

print(f"{day:02d}/09/{year:04d}")