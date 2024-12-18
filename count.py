N = int(input("Number of names: "))  # Number of names input
listed = []  # List to store names
count = 0  # Initialize count to zero

# Collecting names
for i in range(N):
    name = input("Enter name: ")
    listed.append(name)

# Counting occurrences of 'a' in all names
for name in listed:
    count += name.lower().count('a')  # Case insensitive count of 'a'

# Print the total count of 'a'
print("Total occurrences of 'a':", count)
