a = int(input())
b = int(input())

def count_multiples_of_4(start, end):
    count = 0
    for number in range(start, end + 1):
        if number % 4 == 0:
            count += 1
    return count

if a > b:
    a, b = b, a
result = count_multiples_of_4(a, b)
print(result)

