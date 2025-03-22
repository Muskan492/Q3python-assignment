#Control Flow & Loops
age = 20

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

#Loops
    count = 1
while count <= 5:
    print("Count:", count)
    count += 1

    x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  
    print(x)

    for i in range(5):  
        print("Iteration:", i)

        fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")
            for num in range(1, 6):
                if num == 3:
                    break  # Stops the loop when num is 3
                print(num)

            for num in range(1, 6):
                if num == 3:
                    continue  # Skips 3
                print(num)
                    #Lists, Tuples & Dictionary

#Lists, Tuples & Dictionary
# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[0]) 
print(fruits[-1])  

fruits[1] = "blueberry"  
print(fruits)

fruits.append("orange")  
fruits.insert(1, "grape")  
print(fruits)

fruits.remove("grape")  
popped_item = fruits.pop()  
print(fruits, popped_item)

for fruit in fruits:
    print(fruit)

# Tuples 
    colors = ("red", "green", "blue")
print(colors)
print(colors[1])  # Green
print(colors[-1])  # Blue
a, b, c = colors
print(a, b, c)

# Dictionary
student = {"name": "Alice", "age": 22, "grade": "A"}
print(student)
print(student["name"])  
print(student.get("age"))  

student["age"] = 23  
student["city"] = "New York" 
print(student)

student.pop("city")  
del student["grade"]  
print(student)

for key, value in student.items():
    print(key, ":", value)

#Set & Frozenset
fruits = {"orange", "mango", "apple"}
print(fruits)

fruits.add("banaba")  # Add a new element
fruits.remove("apple")  # Remove an element
print(fruits)

print("apple" in fruits)  # True
print("grape" in fruits)  # False

# Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  
print(A & B)  
print(A - B)  
print(A ^ B)  

# Frozenset
numbers = frozenset([1, 2, 3, 4])
print(numbers)

A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])

print(A | B)  
print(A & B)  
print(A - B)  
print(A ^ B)  
