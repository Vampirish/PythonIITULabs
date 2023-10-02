print(f"Task 1")
num = int(input())
if (num // 1000 + num % 10) == abs(num // 100 % 10 - num // 10 % 10):
    print("yes")
else:
    print("no")

print(f"\nTask 2")
age = int(input())
if age < 18:
    print("Access is denied")
else:
    print("Access is allowed")

print(f"\nTask 3")
x1 = int(input())
x2 = int(input())
x3 = int(input())
if x2 - x1 == x3 - x2:
    print("YES")
else:
    print("NO")

print(f"\nTask 4")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")

print(f"\nTask 5")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 == x2 and (y1 == y2-1 or y1 == y2+1)) or (y1 == y2 and (x1 == x2-1 or x1 == x2+1)) or \
        ((x1 == x2-1 or x1 == x2+1) and (y1 == y2-1 or y1 == y2+1)):
    print("YES")
else:
    print("NO")

print(f"\nTask 6")
x1 = int(input())
x2 = int(input())
x3 = int(input())
print(max(x1, max(x2, x3)) - min(x1, min(x2, x3)))

print(f"\nTask 7")
month = int(input())
if month == 2:
    print(28)
elif month == 4 and month == 6 and month == 9 and month == 11:
    print(30)
else:
    print(31)

print(f"\nTask 8")
weight = int(input())
if weight < 60:
    print("Light weight")
elif weight < 64:
    print("First welterweight")
else:
    print("Welterweight")

print(f"\nTask 9")
pass1 = input()
pass2 = input()
if pass1 == pass2:
    print("Password accepted")
else:
    print("Password not accepted")

print(f"\nTask 10")
x = int(input())
if x % 2 == 0:
    print("Even value")
else:
    print("Odd number")

print(f"\nTask 11")
x1 = int(input())
x2 = int(input())
print(min(x1, x2))

print(f"\nTask 12")
age = int(input())
if age < 13:
    print("inclusive-childhood")
elif age < 25:
    print("youth")
elif age < 59:
    print("maturity")
else:
    print("old age")

print(f"\nTask 13")
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Equailatereal')
elif a == b != c or a == c != b or b == c != a:
    print('Isosceles')
else:
    print('Versatile')