def validate_passwords(password_list, selected_criteria):
    valid_special_chars = {'!', '@', '#'}
    criteria_messages = {
        1: "Uppercase letters missing",
        2: "Lowercase letters missing",
        3: "Numbers missing",
        4: "Special characters missing",
    }
    
    for password in password_list:
        if len(password) < 8:
            print(f"Password '{password}' is Invalid. Less than 8 characters.")
            pass  # Skip to the next password
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
        else:
            print(f"Password '{password}' is Valid.")

# Take input from the user
selected_criteria = list(map(int, input("Enter criteria to check (1 for Uppercase, 2 for Lowercase, 3 for Numbers, 4 for Special Characters), separated by commas: ").split(',')))
password_list = input("Enter passwords separated by commas: ").split(',')

# Validate passwords
validate_passwords(password_list, selected_criteria)

