lst = []
s = 0
for element in lst:
    if element < 30 and element % 3 == 0:
        print(element)
    else:
        s += element

print(s)