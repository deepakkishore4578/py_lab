def string_permutations(s):
    n = len(s)
    indices = list(range(n))
    cycles = list(range(n, 0, -1))
    result = []
    s = list(s)

    result.append(''.join(s))  # Add the initial permutation
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                s[i:] = s[i + 1:] + s[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                s[i], s[-j] = s[-j], s[i]
                result.append(''.join(s))
                break
        else:
            break
    return result

# Input and output
string = input("Enter a string: ")
print(f"Permutations of '{string}':")
for perm in string_permutations(string):
    print(perm)
