from prettytable import PrettyTable
table = PrettyTable() # Create a table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l" # Left align
table.add_row(["Bulbasaur", "Grass"]) # Add a row
print(table)


