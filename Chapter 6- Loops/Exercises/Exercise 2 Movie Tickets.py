# Ask for the person's age
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

# Keep asking for age until the person quits
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    # Determine the ticket price based on age
    if age < 3:
        print("  You get in free! Enjoy the show.")
    elif age < 13:
        print("  Your ticket is $10. Have fun!")
    else:
        print("  Your ticket is $15. Enjoy the performance!")
