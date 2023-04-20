rivers = {
    'amazon': 'brazil',
    'mekong': 'vietnam',
    'danube': 'europe',
    'ganges': 'india',
    'volga': 'russia',
}

# print out a statement for each river and its corresponding country
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# print out a list of rivers in the data set
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

# print out a list of countries in the data set (using set to remove duplicates)
print("\nThe following countries are included in this data set:")
for country in set(rivers.values()):
    print(f"- {country.title()}")