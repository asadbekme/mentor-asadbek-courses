n, k = map(int, input().split())
a = list(map(int, input().split()))

b = sorted(a)
print(b[k-1])