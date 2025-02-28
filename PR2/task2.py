import random
array = random.choices(range(100, 1000), k=10)
count = 0
for item in array:
    if item % 2 == 0:
        count += 1

print(array)
print(count)
