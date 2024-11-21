def unitary_sum(n):
    while n >= 10:  # Repeat until a single digit is obtained
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10  # Add the last digit
            n //= 10  # Remove the last digit
        n = digit_sum
    return n

# Input and output
num = int(input("Enter an integer: "))
result = unitary_sum(num)
print(f"The Unitary Sum of Digits of {num} is: {result}")

