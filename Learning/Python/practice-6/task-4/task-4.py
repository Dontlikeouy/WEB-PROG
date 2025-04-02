print("Input file contains:")
letters=0
words=0
lines=0
with open("file.txt",'r', encoding="utf-8") as file:
    for line in file:
        line=line.strip()
        lines+=1
        words+=len(line.split(" "))
        letters+=len(line.replace(" ",'').replace(".",''))
print(letters,"letters")
print(words,"words")
print(lines,"lines")
