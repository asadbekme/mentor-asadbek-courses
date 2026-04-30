def max_2(*args):
    max_1 = max(args)
    args = list(args)
    args.remove(max_1)
    max_2 = max(args)
    return max_2

print(max_2(1, 2, 3, 4, 5))