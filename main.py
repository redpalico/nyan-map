import random

# Define the terrains and their corresponding alphabets
terrains = {
    "G": "Grassland",  # 草原
    "W": "Water",      # 水
    "F": "Forest",     # 森
    "D": "Desert",     # 砂漠
    "M": "Mountain"    # 山
}

# Create a 6x6 grid with random terrains
grid = [[random.choice(list(terrains.keys())) for _ in range(6)] for _ in range(6)]

# Display the grid as text
for row in grid:
    print("".join(row))
