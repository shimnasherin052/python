# Taking input for the marks of each student
a = float(input("Enter the marks of A: "))
b = float(input("Enter the marks of B: "))
c = float(input("Enter the marks of C: "))
d = float(input("Enter the marks of D: "))
e = float(input("Enter the marks of E: "))

# Calculating the total marks
total = a + b + c + d + e
print("Total:", total)

# Calculating the percentage
percentage = (total / 500) * 100  # Since the total marks are out of 500 (5 students * 100 marks each)
print("Percentage:", percentage)
