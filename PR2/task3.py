array = [1, 3, 5, 6, 7, 8]
array2 = []
for item in range(1, len(array)+1):
    array2.append(array[-item])
print(array2)
