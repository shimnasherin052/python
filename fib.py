def fibonacci(n):
    a, b = 1, 1
    while a < n:
        print(a)
        a, b = b, a + b

# Get user input
n = int(input("Enter the number: "))
fibonacci(n)
