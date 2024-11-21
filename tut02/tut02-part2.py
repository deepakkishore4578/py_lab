def compress_string(s):
    compressed = ""  # Initialize compressed string
    count = 1  # Counter for consecutive characters

    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:  # Check for consecutive characters
            count += 1
        else:
            compressed += s[i] + str(count)  # Add character and count to compressed string
            count = 1  # Reset counter for the next character
    
    return compressed

# Input and output
string = input("Enter a string: ")
compressed_result = compress_string(string)
print(f"Compressed string: {compressed_result}")
