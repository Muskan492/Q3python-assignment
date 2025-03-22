#Control Flow
#Conditional Statements if-elif-else
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(10)) 
print(check_number(-5)) 
print(check_number(0))   

#Loops
#For Loop
for i in range(3):
    print(f"Iteration {i}")

#While Loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1


#Functions
#Defining and Calling a Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Muskan"))  

#Function with Default Arguments
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())        
print(greet("Ali"))    

#Lambda Function
square = lambda x: x * x
print(square(4))  


#Math, Date, and Calendar Modules 
#Math Module
import math
#Common Math Functions
import math

print(math.sqrt(25))     
print(math.pow(2, 3))    
print(math.factorial(5)) 
print(math.ceil(4.3))    
print(math.floor(4.8))   
print(math.pi)           
print(math.e)          

#Trigonometric Functions
import math

angle = math.radians(30)  
print(math.sin(angle))    
print(math.cos(angle))    
print(math.tan(angle))   

#Date & Time Module
from datetime import datetime

now = datetime.now()
print("Current Date & Time:", now)  

from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  
print("Formatted Date & Time:", formatted_time)  



from datetime import datetime

now = datetime.now()
print("Year:", now.year)  
print("Month:", now.month)  
print("Day:", now.day)  
print("Hour:", now.hour)  
print("Minute:", now.minute)  
print("Second:", now.second)  

from datetime import datetime, timedelta

today = datetime.now()
future_date = today + timedelta(days=10)  # Add 10 days
print("Future Date:", future_date.strftime("%Y-%m-%d"))  


#Calendar Module
import calendar

year = 2025
month = 3
print(calendar.month(year, month))

import calendar

year = 2024
print(calendar.isleap(year)) 

import calendar

year = 2025
print(calendar.calendar(year))
