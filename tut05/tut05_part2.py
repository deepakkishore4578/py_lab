def is_balanced(s):
    stack = []  # Stack to keep track of opening brackets
    pairs = {')': '(', ']': '[', '}': '{'}  # Matching pairs of brackets

    for char in s:
        if char in "([{":  # If the character is an opening bracket
            stack.append(char)
        elif char in ")]}":  # If the character is a closing bracket
            if not stack or stack[-1] != pairs[char]:
                return False  # Unmatched closing bracket
            stack.pop()  # Remove the matched opening bracket

    return not stack  # If stack is empty, the string is balanced

# Input and Output
s = input("Enter a string containing parentheses: ")

if is_balanced(s):
    print("The input string is balanced.")
else:
    print("The input string is NOT balanced.")
