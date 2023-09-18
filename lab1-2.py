print(f"Task 1.1")
print("4 8 15 16 23 42")

print(f"\nTask 1.2")
print(f"4\n8\n15\n16\n23\n42")

print(f"\nTask 1.3")
x = int(input())
print(x, x+1, x+2, sep='\n')

print(f"\nTask 1.4")
x = int(input())
y = int(input())
z = int(input())
print(x + y + z)

print(f"\nTask 1.5")
a = int(input())
print("Volume =", a**3)
print("Total surface area =", a**2 * 6)

print(f"\nTask 2.1")
n = int(input())
k = int(input())
print(k // n, '\n', k % n, sep='')

print(f"\nTask 2.2")
x = int(input())
print("The digit in the thousands position is", x // 1000)
print("The number in the hundreds position is", x // 100 % 10)
print("The digit in the tens position is", x // 10 % 10)
print("The digit in the position of units is", x % 10)

print(f"\nTask 2.3")
n = int(input())
print((n % 2 + n) // 2)

print(f"\nTask 2.4")
x = int(input())
if x << x == 0:
    print("Warning!!!, The result of << is 0")
else:
    print("The result of << is", x << x)

print(f"\nTask 2.5")
print("Please enter the first number: ", end='')
x1 = int(input())
print("Please enter the second number: ", end='')
x2 = int(input())
print("Please choose the operation (+, -, *, /) : ", end='')
operation = input()
if operation == '+':
    print(x1 + x2)
elif operation == '-':
    print(x1 - x2)
elif operation == '*':
    print(x1 * x2)
elif operation == '/':
    print(x1 / x2)