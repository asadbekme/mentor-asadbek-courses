def argv_int(*args):
    count = 0
    for arg in args:
        if type(arg) == int:
            count += 1
    return count

print(argv_int(1, 2.0, 3, 'a', 'b', None))  # 3
print(argv_int())  # 0
