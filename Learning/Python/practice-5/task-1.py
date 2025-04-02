def nat(m,n):
    print(m)
    if m!=n:
        nat(m+1,n)

m=1
n=5

nat(m,n)