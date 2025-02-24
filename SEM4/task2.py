def sum_range(start, end):
    if start > end:
        start, end = end, start
    result = 0
    while (start <= end):
        result += start
        start += 1
    return (result)


print(sum_range(3, 5))
