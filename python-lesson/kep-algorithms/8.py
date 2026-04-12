# print(reversed('hello world')) # <reversed object>
# print(list(reversed('hello world'))) # ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']

n = int(input())
s = str(n)

count = 0
for ch in reversed(s):
    if ch == '0':
        count += 1
    else:
        break

print(count)