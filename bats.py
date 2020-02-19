# Bat name abbreviation
# Feb/18/2020
# swarup

# There are three species of bats
# Myotis austroriparius
# Myotis septentrionalis
# Eptesicus fuscus


# Input full name of the species
species1 = input("Type in species 1 name: ")
species2 = input("Type in species 2 name: ")
species3 = input("Type in species 3 name: ")

# abbreviate in all caps in each species using 1st letter of genus and species
sp1 = (species1.split(" ")[0][0:3] + species1.split(" ")[1][0:3]).upper()
sp2 = (species2.split(" ")[0][0:3] + species2.split(" ")[1][0:3]).upper()
sp3 = (species3.split(" ")[0][0:3] + species3.split(" ")[1][0:3]).upper()

# output
print(sp1 + "\n" + sp2 + "\n" + sp3 + "\n")
