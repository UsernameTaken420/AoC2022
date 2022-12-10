def getCommon(partOne, partTwo):
    sharedItems = []
    for item in partOne:
        if item in partTwo and item not in sharedItems:
            sharedItems += item
    return sharedItems

def getPriority(char):
    priority = ord(char) - 96
    if priority < 1:
        priority += 58
    return priority

file = open("input.txt", "r")
totalSum = 0
for row in file:
    compOne = row[0:(int((len(row))/2))]
    compTwo = row[int((len(row))/2):]
    for item in getCommon(compOne, compTwo):
        totalSum += getPriority(item)
print(f"{totalSum}")