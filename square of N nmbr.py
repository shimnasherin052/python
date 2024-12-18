N = int(input("Enter total number of elements in list: "))
numbers = [] 

# Getting input from the user and storing in 'numbers'
for i in range(N):
    value = int(input("Enter a number: "))
    numbers.append(value)

# Printing the square of each number in the list
for i in numbers:
    print("Square of", i, "is:", pow(i, 2))
