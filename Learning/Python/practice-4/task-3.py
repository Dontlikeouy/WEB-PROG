stri="шалаш"

for i in range(len(stri)//2):
    if stri[i]!=stri[len(stri)-i-1]:
        print('НЕТ')
        exit(0)
print('ДА')
