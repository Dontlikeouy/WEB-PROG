userInput = input().split(", ")

if userInput.count != 2:
    exit(0)

X, Y = int(userInput[0]), int(userInput[1])

if X == 0 or Y == 0:
    exit(0)

if X > 0 and Y > 0:
    print(1)
elif X < 0 and Y > 0:
    print(2)
elif X < 0 and Y < 0:
    print(3)
elif X > 0 and Y < 0:
    print(4)
