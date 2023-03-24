# Define a list of places to visit
places_to_visit = ['Japan', 'Australia', 'Egypt', 'Brazil', 'Canada']

# Print the list in its original order
print("Original order:")
print(places_to_visit)

# Print the list in alphabetical order using sorted()
print("\nAlphabetical order:")
print(sorted(places_to_visit))

# Show that the original order is still intact
print("\nOriginal order:")
print(places_to_visit)

# Print the list in reverse alphabetical order using sorted()
print("\nReverse alphabetical order:")
print(sorted(places_to_visit, reverse=True))

# Show that the original order is still intact
print("\nOriginal order:")
print(places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()

# Print the list to show the changed order
print("\nReversed order:")
print(places_to_visit)

# Change the order of the list again using reverse()
places_to_visit.reverse()

# Print the list to show that it's back to its original order
print("\nOriginal order:")
print(places_to_visit)

# Sort the list in alphabetical order using sort()
places_to_visit.sort()

# Print the list to show the new order
print("\nAlphabetical order:")
print(places_to_visit)

# Sort the list in reverse alphabetical order using sort()
places_to_visit.sort(reverse=True)

# Print the list to show the new order
print("\nReverse alphabetical order:")
print(places_to_visit)
