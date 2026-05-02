def params(*args, **kwargs):
    return len(args) + len(kwargs)

print(params(1, 2, 3, a=4, b='x', d=None))  # 6
print(params())  # 0