def params_dict(*rgs, **kwargs):
    int_count, bool_count, float_count, str_count = 0, 0, 0, 0
    for arg in rgs:
        if type(arg) == int:
            int_count += 1
        elif type(arg) == bool:
            bool_count += 1
        elif type(arg) == float:
            float_count += 1
        elif type(arg) == str:
            str_count += 1
    for key, value in kwargs.items():
        if type(value) == int:
            int_count += 1
        elif type(value) == bool:
            bool_count += 1
        elif type(value) == float:
            float_count += 1
        elif type(value) == str:
            str_count += 1

    return {'int': int_count, 'bool': bool_count, 'float': float_count, 'str': str_count}

print(params_dict(1, 2.0, 'a', a=3, b=False, c=4.5))  # {'int': 2, 'bool': 1, 'float': 2, 'str': 1}
print(params_dict())  # {'int': 0, 'bool': 0, 'float': 0, 'str': 0}