def roundResult(opPlay, mePlay):
    match opPlay:
        case "A": #rock
            opPlay = 1
        case "B": #paper
            opPlay = 2
        case "C": #scissors
            opPlay = 3
    match mePlay:
        case "X": #rock
            points = 1
        case "Y": #paper
            points = 2
        case "Z": #scissors
            points = 3
    if (opPlay == 3 and points == 1):
        points += 6
    elif (opPlay == 1 and points == 3):
        points += 0
    else:
        if (opPlay == points):
            points += 3
        elif (opPlay < points):
            points += 6
    return points

file = open("input.txt", "r")
totalScore = 0
for round in file:
    totalScore += roundResult(round[0], round[2])
print(totalScore)