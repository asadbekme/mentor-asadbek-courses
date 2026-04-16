def sum_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
print(sum_digits(12345))  # Output: 15