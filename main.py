import random

# Define the terrains and their corresponding alphabets
terrains = {
    "G": "Grassland",
    "W": "Water",
    "F": "Forest",
    "D": "Desert",
    "M": "Mountain"
}

# Create a 6x6 grid with random terrains
grid = [[random.choice(list(terrains.keys())) for _ in range(6)] for _ in range(6)]

# Replace "W" with "*" to indicate water terrains distinctly
for i in range(6):
    for j in range(6):
        if grid[i][j] == "W":
            grid[i][j] = "*"

# Display the grid as text with spaces between each character
for row in grid:
    print(" ".join(row))
