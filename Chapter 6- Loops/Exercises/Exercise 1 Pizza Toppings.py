prompt = "\nWhat toppings would you like on your pizza?"

#Append the message to allow users to quit the program
prompt += "\nEnter 'quit' when you are finish deciding: "

#Run a loop to get the user's input on their pizza toppings
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break