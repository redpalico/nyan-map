import random

# Define the terrains and their corresponding alphabets
terrains = {
    "G": "Grassland",
    "*": "Water",
    "F": "Forest",
    "D": "Desert",
    "M": "Mountain"
}

# Create a 7x7 grid with random terrains
grid = [[random.choice(list(terrains.keys())) for _ in range(7)] for _ in range(7)]

# Ensure the center is not water to allow player's placement
grid[3][3] = "G"

# Set the player's initial position to the center of the grid
player_pos = [3, 3]

# Function to display the grid
def display_grid():
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if [i, j] == player_pos:
                print("P", end=" ")
            else:
                print(cell, end=" ")
        print()

# Function to handle player's movement
def move_player(direction):
    x, y = player_pos
    if direction == "W" and x > 0 and grid[x-1][y] != "*":
        x -= 1
    elif direction == "S" and x < 6 and grid[x+1][y] != "*":
        x += 1
    elif direction == "A" and y > 0 and grid[x][y-1] != "*":
        y -= 1
    elif direction == "D" and y < 6 and grid[x][y+1] != "*":
        y += 1
    player_pos[0], player_pos[1] = x, y

# Main loop to interact with the player
while True:
    display_grid()
    command = input("Move with WASD or press P to exit: ").upper()
    if command in "WASD":
        move_player(command)
    elif command == "P":
        break
    else:
        print("Invalid command. Please use WASD to move or P to exit.")
