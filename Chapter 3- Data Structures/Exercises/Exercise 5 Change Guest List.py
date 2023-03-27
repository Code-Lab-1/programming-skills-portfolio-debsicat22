
# Defining a list of people to invite to dinner
guests = ["Leonardo Dicaprio", "Lady Gaga", "Christian Dave Sicat"]

# Printing an invitation message to each person in the list
for guest in guests:
    print("Dear " + guest + ",\nYou are cordially invited to a dinner party on Saturday night. Please let us know if you can make it.\n\nSincerely,\nThe Hosts\n")

# Printing the name of the guest who can't make it
print(guests[1] + " can't make it to the dinner.\n")

# Replacing the name of the guest who can't make it with a new person
guests[1] = "Coco Martin"

# Printing a second set of invitation messages for the remaining guests in the list
for guest in guests:
    print("Dear " + guest + ",\nYou are cordially invited to a dinner party on Saturday night. Please let us know if you can make it.\n\nSincerely,\nThe Hosts\n")
