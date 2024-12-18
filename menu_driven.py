numbers = []

while True:
    print("\nMenu:")
    print("1. Enter a list of numbers")
    print("2. Find the greatest and lowest number")
    print("3. Sort the list in ascending order")
    print("4. Create a list of even numbers")
    print("5. Exit")
    
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        n = int(input("Enter the number of elements in the list: "))
        numbers = []
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        print("List entered:", numbers)
    
    elif choice == 2:
        if numbers:
            greatest = max(numbers)
            lowest = min(numbers)
            print(f"Greatest number: {greatest}")
            print(f"Lowest number: {lowest}")
        else:
            print("No numbers entered yet.")
    
    elif choice == 3:
        if numbers:
            sorted_numbers = sorted(numbers)
            print("Sorted list in ascending order:", sorted_numbers)
        else:
            print("No numbers entered yet.")
    
    elif choice == 4:
        if numbers:
            even_numbers = [num for num in numbers if num % 2 == 0]
            print("List of even numbers:", even_numbers)
        else:
            print("No numbers entered yet.")
    
    elif choice == 5:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
