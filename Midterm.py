print(f"User input, code output [3.333%]")
name = input("Enter your name please: ")
salary = input("Enter your desired salary level:")
if not salary.isdigit():
    print(f"{name}, please enter your desired salary as a digit.")
else:
    taxLevel = int(int(salary) * 0.2)
    print(f"{name}, the tax level you will pay with the salary {salary} is {taxLevel}")


print(f"\nUsing arithmetic, bitwise and logic ops [6.667%]")
Addition = lambda a, b: a + b
Multiplication = lambda a, b: a * b
Division = lambda  a, b : a / b
Exponentiation = lambda a, b : a ** b
operation = int(input())
print("Please enter two numbers for addition, comma separated")
numbers = input().split(", ")
numbers = [int(i) for i in numbers]
if operation == 1:
    print(Addition(numbers[0], numbers[1]))
elif operation == 2:
    print(Multiplication(numbers[0], numbers[1]))
elif operation == 3:
    print(Division(numbers[0], numbers[1]))
elif operation == 4:
    print(Exponentiation(numbers[0], numbers[1]))
else:
    print("Incorrect Input")


print(f"\nLoops and iterations [10%]")
print("Please enter the length of Fibonacci sequence")
n = int(input())
print(f"The Fibonacci sequence for {n} is")
n1 = 1
n2 = 1
print(n1, end=', ')
for i in range(1, n):
    if i == n-1:
        print(n2)
    else:
        print(n2, end=', ')
    x = n2
    n2 = n1 + n2
    n1 = x


print(f"\nTuples and sets [13.333%]")
unique = set()
noUnique = {}
print("Please chose the task you want to perform:")
print("1. Enter items")
print("2. Exit")
operation = int(input())
while operation != 2:
    if operation == 1:
        print("Please enter items separated by comma")
        arr = input().lower().split(", ")
        for i in arr:
            if i in unique:
                noUnique[i] = noUnique.get(i, 0) + 1
            else:
                unique.add(i)
        print("Items are saved")
        noUnique = tuple(((i, cnt) for (i, cnt) in noUnique.items()))
        print("Unique items:", unique)
        print("Not unique items: ", noUnique)

    print("Please chose the task you want to perform:")
    print("1. Enter items")
    print("2. Exit")
    operation = int(input())

print(f"\nLists and dictionaries [16.667%]")
tasks = {}
while True:
    print("Please choose the task you want to perform:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View All Completed Tasks")
    print("5. Exit")

    operation = int(input())

    if operation == 1:
        print("Enter the task: ")
        task = input()
        tasks[task] = False
        print(f"The task “{task}” was added to the todo")
    elif operation == 2:
        print("All Tasks")
        for i in tasks.keys():
            print(f"{i} is {'Done' if tasks[i] else 'Not done'}")
    elif operation == 3:
        print("Write Name of task")
        task = input()
        if task in tasks:
            tasks[task] = True
    elif operation == 4:
        print("All completed tasks")
        for i in tasks.keys():
            if tasks[i]:
                print(i)
    elif operation == 5:
        break
    else:
        print("Incorrect input")