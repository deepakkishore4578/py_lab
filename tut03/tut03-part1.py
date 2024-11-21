# lab 3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def rotate_number(num):
    rotations = []
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()
    
    length = len(digits)
    for i in range(length):
        rotation = 0
        for j in range(length):
            rotation = rotation * 10 + digits[(i + j) % length]
        rotations.append(rotation)
    return rotations

def is_rotational_prime(num):
    rotations = rotate_number(num)
    for rotation in rotations:
        if not is_prime(rotation):
            return False
    return True

# Input and output
num = int(input("Enter a number: "))
if is_rotational_prime(num):
    print(f"{num} is a Rotational prime.")
else:
    print(f"{num} is not a Rotational prime.")
