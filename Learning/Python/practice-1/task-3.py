userInput = int(input())

# 10 < input < 99
if 10 < userInput and userInput < 99:
    print(max(userInput % 10, userInput // 10))