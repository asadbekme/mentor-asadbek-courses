n = int(input())
a = list(map(int, input().split()))
b = []
for element in a:
    if a.count(element) >= 2 and element not in b:
        b.append(element)

print(max(b))