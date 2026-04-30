n = int(input())
s, i = 0, 0
while i < n:
    a = int(input())
    if a % 2 == 1:
        s += a
    i += 1
print(s)