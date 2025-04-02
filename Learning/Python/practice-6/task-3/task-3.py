def read_csv(filePath):
    with open(filePath,'r', encoding="utf-8") as file:
        lines=file.read().splitlines()
        title=lines[0].replace('"',"").strip(',').split(',')
        for i in range(1,len(lines)):
            text=lines[i].replace('"',"").strip(',').split(',')
            for j in range(len(title)):
                print(title[j]+":",text[j])

read_csv("table.csv")
