file = open("input.txt", "r")
for round in file:
    match round[0]:
        case "A":
            print("A")
