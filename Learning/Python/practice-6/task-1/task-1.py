def longest_words(filePath):
    maxLen=0
    text=""
    with open(filePath,'r', encoding="utf-8") as file:
        for line in file:
            if maxLen < len(line):
                maxLen=len(line)
                text=line
    return text

print(longest_words("article.txt"))

