print("hello world")
#def app():

# Display text or variables


# Get length of an object
print(len([1, 2, 3]))




# Generate a sequence (range)
print(list(range(5)))  # [0, 1, 2, 3, 4]

# Convert to string, integer, and float
print(str(100))
print(int("42"))
print(float("3.14"))

# Create a list and dictionary
my_list = list((1, 2, 3))
print(my_list)

my_dict = dict(name="Alice", age=25)
print(my_dict)

# Conditional execution
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# For loop: iterate over elements
for item in [1, 2, 3]:
    print(item)

# While loop: execute while condition is true
y = 3
while y > 0:
    print(y)
    y -= 1

# Add to a list
my_list.append(4)
print(my_list)

# Split a string
print("apple,banana,cherry".split(","))

# Join elements into a string
print(" ".join(["Hello", "World"]))

# Sort elements in place
nums = [3, 1, 2]
nums.sort()
print(nums)

# Find maximum and minimum values
print(max(nums))
print(min(nums))

# Calculate sum of elements
print(sum(nums))

# Pair elements from multiple iterables
names = ["Alice", "Bob"]
ages = [25, 30]
print(list(zip(names, ages)))
