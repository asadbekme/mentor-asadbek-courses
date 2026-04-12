savol = "Yoshingiz nechida? Yoshingizni kiriting, sizga chipta narxini chiqarib beraman: "

while True:
    print("Agar 'exit' yoki 'quit' deb yozsangiz, dastur to'xtaydi.")
    yosh = input(savol)
    if yosh == 'exit' or yosh == 'quit':
        print("Dastur to'xtadi.")
        break
    yosh = int(yosh)

    if yosh < 7:
        narx = 2000
    elif yosh < 18:
        narx = 3000
    elif yosh <= 65:
        narx = 10000
    else:
        narx = 0

    print(f"Sizga chipta narxi {narx} so'm.")