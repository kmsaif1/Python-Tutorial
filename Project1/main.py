import random

# Mapping
youDist = {"s": 1, "w": -1, "g": 0}
revMap = {1: "Snake", -1: "Water", 0: "Gun"}

# Computer randomly picks
computer = random.choice([1, -1, 0])

# Get user input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Validate input
if youstr not in youDist:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = youDist[youstr]

    print(f"Computer chose {revMap[computer]}")
    print(f"You chose {revMap[you]}")

    if computer == you:
        print("It's a DRAW!")
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        print("YOU LOSE!")
    else:
        print("YOU WIN!")
