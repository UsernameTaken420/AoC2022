def getCommon(partOne, partTwo):
    sharedItems = []
    for item in partOne:
        if item in partTwo and item not in sharedItems:
            sharedItems += item
    print(f"{sharedItems}")
    return sharedItems

file = open("testInput.txt", "r")
for row in file:
    compOne = row[0:(int((len(row))/2))]
    compTwo = row[int((len(row))/2):]
    getCommon(compOne, compTwo)
