def kwargv(**kwargs):
    return len(kwargs)

print(kwargv(a=1, b=2, c=3))  # 3
print(kwargv(a=1, b=2, c=3, d=4, e=5))  # 5