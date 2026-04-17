def check_string(string):
    if string.isupper():
        return True
    elif string[0].islower() and string[1:].isupper():
        return True
    else:
        return False
    
s = input()
print(check_string(s))