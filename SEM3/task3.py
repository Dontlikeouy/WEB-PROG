# Напиишите программу, которая принимает на вход два числа и выдаёт какое из них чётное
# в случае одинаковой чётности вывести оба числа

first, second = int(input()), int(input())

if first % 2 == 0 and second % 2 == 0:
    print(first, " ", second)
elif first % 2 == 0:
    print(first)
elif second % 2 == 0:
    print(second)
else:
    print("error")
