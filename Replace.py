greaterThan = "&gt;"
lessThan = "&lt;"

findGreater = ">"
findLess = "<"

for x in range(400):
    y = x + 1
    chapter = "Chapter" + str(y) + ".txt"
    with open(chapter, 'r', encoding="utf-8") as file:
        data = file.read()
        data = data.replace(findGreater, greaterThan)
        data = data.replace(findLess, lessThan)

    with open(chapter, 'w', encoding="utf-8") as file:
        file.write(data)