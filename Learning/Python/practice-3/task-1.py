array = [10, 21, 14, 93, 23]
# 20 <= item <=90
count = 0
for item in range(len(array)):
    if (20 <= array[item] and array[item] <= 90):
        count += 1
print(count)
