def roundResult(opPlay, mePlay):
    match opPlay:
        case "A":
            opPlay = 1
        case "B":
            opPlay = 2
        case "C":
            opPlay = 3
    match mePlay:
        case "X":
            points = 1
        case "Y":
            points = 2
        case "Z":
            points = 3
    if (points > opPlay):
        points += 6
    elif (points == opPlay):
        points += 3
    return points

file = open("testInput.txt", "r")
totalScore = 0
for round in file:
    totalScore += roundResult(round[0], round[2])
print(totalScore)