N = int(input("Enter total number of elements in the list: "))
numbers = []  

# Taking input and storing it in 'numbers'
for i in range(N):
    value = int(input("Enter a number: "))
    numbers.append(value)

# Filtering the positive numbers from the list
positive_numbers = [each for each in numbers if each > 0]
print("Positive numbers:", positive_numbers)

# Alternatively, printing positive numbers using a for loop
print("Positive numbers (using for loop):")
for number in numbers:
    if number > 0:
        print(number)


