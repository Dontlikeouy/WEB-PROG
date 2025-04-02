arr=[1,2,5,10,34]

def rec(i=0):
    if len(arr)==i:
        return
    else:    
        print(arr[len(arr)-i-1])
        rec(i+1)


rec()