n, x = map(int, input().split())
a = list(map(int, input().split()))
for element in a:
    if element % 2 != 0:
        print(element, end = " ")
    if element == x:
        break

    




    