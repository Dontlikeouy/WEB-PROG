userInput = ''
sum = 0
while (True):
    userInput = input()
    if userInput == 'q':
        break
    sum = 0
    for item in userInput:
        sum += int(item)
    if sum % 2 == 0:
        break
