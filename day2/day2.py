def roundResult(opPlay, mePlay): #according to part 1
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

def altResult(opPlay, result): #according to part 2
    match opPlay:
        case "A": #rock
            opPlay = 1
        case "B": #paper
            opPlay = 2
        case "C": #scissors
            opPlay = 3
    match result:
        case "X": #lose
            if (opPlay == 1):
                points = 3
            elif (opPlay == 2):
                points = 1
            else:
                points = 2
        case "Y": #draw
            points = opPlay + 3
        case "Z": #win
            if (opPlay == 1):
                points = 2
            elif (opPlay == 2):
                points = 3
            else:
                points = 1
            points += 6
    return points

file = open("input.txt", "r")
totalScorePartOne = 0
totalScorePartTwo = 0
for round in file:
    totalScorePartOne += roundResult(round[0], round[2])
    totalScorePartTwo += altResult(round[0], round[2])
print(f"{totalScorePartOne}, {totalScorePartTwo}")