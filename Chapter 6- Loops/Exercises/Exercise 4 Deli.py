sandwich_orders = ['veggies', 'cheese', 'bacon', 'barbecue']
finished_sandwiches = []

# Loop through each sandwich order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    # Ask the user if they want the current sandwich
    message = f"I'm working on your {current_sandwich} sandwich. Would you like it? (yes/no): "
    response = input(message)
    
    # If yes, add it to finished sandwiches list
    if response.lower() == 'yes':
        finished_sandwiches.append(current_sandwich)
        print(f"Added {current_sandwich} sandwich to finished sandwiches.")
    # If no, continue to next sandwich order
    else:
        print(f"Discarded {current_sandwich} sandwich.")
    
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
