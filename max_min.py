list1 = input("Enter a list of numbers (space-separated): ")
list2 = list(map(int, list1.split()))  # Converting input to a list of integers

# Sorting the list
sort1 = sorted(list2)
print("Sorted list:", sort1)

# Finding the maximum and minimum values
max1 = max(list2)
print("Maximum value:", max1)

min1 = min(list2)
print("Minimum value:", min1)

# Reversing the sorted list
sort1.reverse()
print("Reversed sorted list:", sort1)

# Length of the list
count = len(list2)
print("Length of list:", count)

# Sum of the list elements
sum_of_elements = sum(list2)
print("Sum of list elements:", sum_of_elements)
