def filter_list(list, a):
    if a == 0:
        return [x for x in list if x % 2 != 0]
    else:
        return [x for x in list if x % 2 == 0]
    
print(filter_list([1, 2, 3, 4, 5, 6], 0))  # [1, 3, 5]
print(filter_list([3, 5, 3, 6], 1))  # [6]