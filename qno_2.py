# inialize empty array
array = []

# How many numbers to be added
n = int(input("Enter the number of elements: "))

# Add n numbers to the array
for i in range(n):
    num = int(input("Enter number: "))
    array.append(num)

# print updated Array
print("Array:", array)