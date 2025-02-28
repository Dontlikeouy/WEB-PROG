userinput = ''
sum = 0
while (True):
    userinput = input()
    if userinput == 'q':
        break
    sum = 0
    for item in userinput:
        sum += int(item)
    if sum % 2 == 0:
        break
