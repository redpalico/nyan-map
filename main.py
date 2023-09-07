import random

# Create a list of terrains
terrains = ["G", "W", "F", "D", "M"]

# Create a 6x6 grid
grid = [[random.choice(terrains) for _ in range(6)] for _ in range(6)]

# Display the grid as text
for row in grid:
    print("".join(row))
