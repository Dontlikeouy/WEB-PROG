def count_bits(n):
    n = str(bin(n)[2:])
    count=0
    for item in n:
        if item=='1':
            count+=1
    return count