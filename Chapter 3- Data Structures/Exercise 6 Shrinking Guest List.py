# create a list of guests to invite to dinner
guest_list = ['Leonardo Dicaprio', 'Lady Gaga', 'Coco Martin', 'Christian Dave Sicat']

# print a message saying only two guests can be invited
print("Unfortunately, the dinner table can only accommodate two guests.")

# remove guests from the list one at a time until only two names remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, we'll have to reschedule our dinner.")

# print invitation messages to the remaining two guests
for guest in guest_list:
    print(f"Dear {guest}, please join me for dinner on Saturday at 7pm.")

# remove the last two names from the list using del
del guest_list[-2:]
print(guest_list)  # should print an empty list
