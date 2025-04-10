def filter_list(l):
    copyl=[]
    for item in l:
        if type(item) != str:
            copyl.append(item)
    return copyl