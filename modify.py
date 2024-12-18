def modify_string(input_string):
    if len(input_string) > 0:  # Check if the input string is non-empty
        first_char = input_string[0]  # Get the first character of the string
        # Replace every occurrence of the first character (except the first one) with '$'
        modified_string = first_char + input_string[1:].replace(first_char, '$')
        return modified_string
    return input_string  # Return the original string if it's empty

input_str = input("Enter a string: ")
result = modify_string(input_str)
print("Modified string:", result)
