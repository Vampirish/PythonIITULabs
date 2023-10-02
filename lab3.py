from collections import Counter
from itertools import combinations, groupby

print(f"Task 1.1")
s = input()
print(tuple(s))

print(f"\nTask 1.2")
t = ('H', 'e', 'l', 'l', 'o')
print(str(t))

print(f"\nTask 1.3")
tupleA = (1, 2, 3, 4, 5, 6, 7)
tupleB = (5, 6, 7, 9, 7, 1, 10, 10)
mdA = len(tupleA) // 2 + len(tupleA) % 2
mdB = len(tupleB) // 2 + len(tupleB) % 2
print(tupleA[:mdA] + tupleB[mdB:])

print(f"\nTask 1.4")
tupleX = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
tupleRes = ()
for i in range(len(tupleX)):
    if tupleX[i] not in tupleX[:i]:
        cnt = 0
        for j in tupleX:
            if j == tupleX[i]:
                cnt += 1
        tupleRes += tuple(((tupleX[i], cnt),))
print(tupleRes)

print("\nTask 1.5")
tupleX = (55, 6, 777, 70.0, "7", "A")
tupleRes = []
tupleY = ()
tupleType = type(tupleX[0])
for i in tupleX:
    xType = type(i)
    if xType != tupleType:
        tupleRes.append(tuple(tupleY))
        tupleY = ()
        tupleType = xType
    tupleY += (i,)
tupleRes.append(tuple(tupleY))
for tupleZ in tupleRes:
    print(tupleZ)

print("\nTask 2.1")
s = input()
print({i for i in s})

print("\nTask 2.2")
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
print(set_A.difference(set_B))

print("\nTask 2.3")
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
set_X = set_A
set_X.difference_update(set_B)
print(set_X)

print("\nTask 2.4")
set_ex = {1, 2, 3, 4, 7}
set_ex1 = {8, 7, 9, 4, 2, 0, 10}
set_ex2 = {4, 0, 1}
for element in set_ex.copy():
    if element in set_ex2:
        set_ex.remove(element)
        set_ex1.add(element)
set_ex2.update(set_ex, set_ex2)
print(set_ex2)

print("\nTask 2.5")
A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5
list_of_sets = []
for combo in combinations(A, n):
    list_of_sets.append(set(combo))
    if len(list_of_sets) == m:
        break
print(list_of_sets)

print("\nTask 3.1")
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]
cars_list.sort(key=lambda x: x[0])
for manufacturer, group in groupby(cars_list, key=lambda x: x[0]):
    count = len(list(group))
    print(manufacturer, count)
    for model in group:
        print(f"- {model[1]}")