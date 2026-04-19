# 1-usul:
# def reverse_number(num):
#     if num < 0:
#         return -reverse_number(-num)
#     else:
#         return int(str(num)[::-1])
    
# 2-usul:
def reverse_number(num):
    if num < 0:
        return -reverse_number(-num)
    else:
        reversed_num = 0
        while num > 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        return reversed_num

# Example usage:
a = int(input())
print(reverse_number(a))