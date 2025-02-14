# напишите программу, которая на вход принимает два числа, а выходе, отдаёт какое число больше, а какое меньше

first = int(input())
second = int(input())

if first == second:
    print("Error")
elif first > second:
    print(str(first), ">")
    print(str(second), "<")
else:
    print(str(second), ">")
    print(str(first), "<")
