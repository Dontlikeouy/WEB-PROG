with open("prices.txt",'r', encoding="utf-8") as file:
    resultSum=0
    for line in file:
        sline=line.replace("\n","").split('\t')
        resultSum+=int(sline[1].replace("шт",""))* float(sline[2].replace("р",""))
    print(resultSum)