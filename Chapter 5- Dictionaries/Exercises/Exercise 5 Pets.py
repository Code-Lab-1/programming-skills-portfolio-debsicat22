# Create an empty list to store the pets in.
pets = []

# Create a dictionary for a pet and append it to the pets list.
pet = {
    'animal type': 'fly',
    'name': 'jarred',
    'owner': 'guy',
    'weight': 5,
    'eats': 'bugs',
}
pets.append(pet)

# Create a dictionary for another pet and append it to the pets list.
pet = {
    'animal type': 'cat',
    'name': 'clare',
    'owner': 'tanjiro',
    'weight': 20,
    'eats': 'slippers',
}
pets.append(pet)

# Create a dictionary for a third pet and append it to the pets list.
pet = {
    'animal type': 'dog',
    'name': 'irso',
    'owner': 'tion',
    'weight': 47,
    'eats': 'meat',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
