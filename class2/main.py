# Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.3333
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

# Comparison Operators
print("Equal:", a == b)          # False
print("Not Equal:", a != b)      # True
print("Greater than:", a > b)    # True
print("Less than:", a < b)       # False
print("Greater than or equal:", a >= b) # True
print("Less than or equal:", a <= b)   # False

# Assignment Operators
x = 5
x += 3   # x = x + 3
print("x after += 3:", x)  # 8
x -= 2   # x = x - 2
print("x after -= 2:", x)  # 6
x *= 2   # x = x * 2
print("x after *= 2:", x)  # 12
x /= 4   # x = x / 4
print("x after /= 4:", x)  # 3.0
x %= 2   # x = x % 2
print("x after %= 2:", x)  # 1.0
x **= 3  # x = x ** 3
print("x after **= 3:", x) # 1.0
x //= 2  # x = x // 2
print("x after //= 2:", x) # 0.0

# Logical Operators
p = True
q = False
print("Logical AND:", p and q) # False
print("Logical OR:", p or q)  # True
print("Logical NOT:", not p)  # False

# Bitwise Operators
m = 5  # 101 in binary
n = 3  # 011 in binary

print("Bitwise AND:", m & n)  # 001 (1)
print("Bitwise OR:", m | n)   # 111 (7)
print("Bitwise XOR:", m ^ n)  # 110 (6)
print("Bitwise NOT (~m):", ~m) # -6
print("Left Shift:", m << 1)  # 1010 (10)
print("Right Shift:", m >> 1) # 10 (2)

# Membership Operators
list1 = [1, 2, 3, 4, 5]
print("Is 3 in list?", 3 in list1)  # True
print("Is 6 not in list?", 6 not in list1) # True

# Identity Operators
x = 10
y = 10
z = [1, 2, 3]
w = [1, 2, 3]

print("x is y:", x is y)       # True (same memory location for small integers)
print("z is w:", z is w)       # False (different lists, different memory locations)
print("z is not w:", z is not w) # True
