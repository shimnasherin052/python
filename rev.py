while True:
    num = input("Enter a number (at least 4 digits): ")
    if num.isdigit() and len(num) >= 4:
        num = int(num)
        break
    else:
        print("Please enter a valid number with at least 4 digits.")

reverse_num = 0
temp_num = num

while temp_num > 0:
    digit = temp_num % 10
    reverse_num = reverse_num * 10 + digit
    temp_num = temp_num // 10

print(f"Original number: {num}")
print(f"Reversed number: {reverse_num}")
