#Exception Handling
#Try-Except



try:
    x = 10 / 0 
except ZeroDivisionError:
    print("Cannot divide by zero!")


#Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")

 #If input is "0" 
 #If input is "abc"


try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter a number.")
else:
    print("Result:", result)  
finally:
    print("Execution completed.")  

# If input is "5":

#Custom Exceptions
class NegativeNumberError(Exception):
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"Number is {num}"

try:
    print(check_positive(-5))
except NegativeNumberError as e:
    print("Error:", e)


#Exception Handling 
try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    if 'file' in locals():
        file.close()
        print("File closed.")

# If "test.txt" doesn't exist:

#File Handling 
file = open("this.txt", "r")

#Writing to a File
file = open("this.txt", "w")  
file.write("Hello, World!\n")
file.write("Python file handling example.")
file.close()  

#Appending to a File
file = open("this.txt", "a")  
file.write("\nThis is a new line.")
file.close()

# Reading from a File
file = open("this.txt", "r")
content = file.read()
print(content)  
file.close()
#Reading Line by Line
file = open("this.txt", "r")
for line in file:
    print(line.strip())  # strip() removes extra newlines
file.close()


#Reading Specific Number of Characters
file = open("this.txt", "r")
print(file.read(5))  
file.close()

file = open("this.txt", "r")
lines = file.readlines()  
print(lines)
file.close()

with open("this.txt", "r") as file:
    content = file.read()
    print(content)  



try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found!")


# Writing binary data
with open("image.jpg", "rb") as source, open("copy.jpg", "wb") as destination:
    destination.write(source.read())
