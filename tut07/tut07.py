def validate_passwords_from_file(password_file, selected_criteria):
    valid_special_chars = {'!', '@', '#'}
    criteria_messages = {
        1: "Uppercase letters missing",
        2: "Lowercase letters missing",
        3: "Numbers missing",
        4: "Special characters missing",
    }
    
    valid_count = 0
    invalid_count = 0
    
    # Open the file and read passwords
    with open(password_file, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()  # Remove any leading/trailing whitespace
        
        if len(password) < 8:
            print(f"Password '{password}' is Invalid. Less than 8 characters.")
            invalid_count += 1
            continue
        
        errors = []
        
        # Check criteria based on user selection
        if 1 in selected_criteria and not any(char.isupper() for char in password):
            errors.append(criteria_messages[1])
        if 2 in selected_criteria and not any(char.islower() for char in password):
            errors.append(criteria_messages[2])
        if 3 in selected_criteria and not any(char.isdigit() for char in password):
            errors.append(criteria_messages[3])
        if 4 in selected_criteria:
            special_chars = [char for char in password if char in valid_special_chars]
            if not special_chars:
                errors.append(criteria_messages[4])
            elif any(char not in valid_special_chars for char in password if not char.isalnum()):
                errors.append("Contains invalid special characters")
        
        # Output the results
        if errors:
            print(f"Password '{password}' is Invalid. {', '.join(errors)}.")
            invalid_count += 1
        else:
            print(f"Password '{password}' is Valid.")
            valid_count += 1
    
    # Display total valid and invalid passwords
    print(f"\nTotal Valid Passwords: {valid_count}")
    print(f"Total Invalid Passwords: {invalid_count}")

# Take input from the user
selected_criteria = list(map(int, input("Enter criteria to check (1 for Uppercase, 2 for Lowercase, 3 for Numbers, 4 for Special Characters), separated by commas: ").split(',')))

# Validate passwords from the input file
validate_passwords_from_file('input.txt', selected_criteria)
