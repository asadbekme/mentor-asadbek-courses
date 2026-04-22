n, x = map(int, input().split())
a = list(map(int, input().split()))
b = []
for element in a:
    if element % 2 != 0:
        b.append(element)
    if element == x:
        break

print(*b)
print(sum(a) - sum(b))

    




    