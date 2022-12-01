calorieList = open("input.txt", "r")
elves = []
elvesCount = 0
elves.append(0)
for item in calorieList:
    if item in ['\n', '\r\n']:
        elves.append(0)
        elvesCount += 1
    else:
        elves[elvesCount] += int(item)
elves.sort()
print(elves)