array = [6, 7, 19, 34, 3, 1, 4, 7, 9, 1]
# 20 <= item <=90
count = 0
for item in range(len(array)):
    if (array[item] % 2 == 0):
        count += 1
print(count)
