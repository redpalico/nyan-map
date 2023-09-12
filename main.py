import random

# Define the terrains and their corresponding symbols
terrains = {
    "G": "Grassland",
    "W": "Water",
    "F": "Forest",
    "D": "Desert",
    "M": "Mountain"
}

# Create a 7x7 grid with random terrains
grid = [[random.choice(list(terrains.keys())) for _ in range(7)] for _ in range(7)]

# Set the player's initial position to the center of the grid
player_pos = [3, 3]

# If the player's initial position is water, change it to grassland
if grid[player_pos[0]][player_pos[1]] == "W":
    grid[player_pos[0]][player_pos[1]] = "G"

def display_grid():
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if [i, j] == player_pos:
                print("P", end=" ")
            else:
                if cell == "W":
                    print("*", end=" ")
                else:
                    print(cell, end=" ")
        print()
    
    # Get the terrain at the player's current position
    current_terrain = terrains[grid[player_pos[0]][player_pos[1]]]
    print(f"The player is currently on {current_terrain}.")
    print()  # Print an empty line

# Function to move the player
def move_player(direction):
    x, y = player_pos
    if direction == "W" and x > 0 and grid[x-1][y] != "W":
        player_pos[0] -= 1
    elif direction == "A" and y > 0 and grid[x][y-1] != "W":
        player_pos[1] -= 1
    elif direction == "S" and x < 6 and grid[x+1][y] != "W":
        player_pos[0] += 1
    elif direction == "D" and y < 6 and grid[x][y+1] != "W":
        player_pos[1] += 1

# Main loop
while True:
    display_grid()
    command = input("Move with WASD or press P to exit: ").upper()
    if command == "P":
        break
    move_player(command)
