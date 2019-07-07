data = [int(input()), int(input()), int(input())]
print("You can NOT run the game" if data[0] < 5 or data[1] < 2 or data[2] < 50 else "You can run the game")