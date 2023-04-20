sandwich_orders = [
    'pastrami', 'barbecue', 'cheese', 'pastrami',
    'bacon', 'beef', 'pastrami']
finished_sandwiches = []

# Display message that pastrami is not available
print("Sorry, we're all out of pastrami today. We'll remove it from your order.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Make all other sandwiches on the sandwich_orders list
print("\n")
if sandwich_orders:
    print("We'll start making your sandwiches now.")
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f"I'm working on your {current_sandwich} sandwich.")
        finished_sandwiches.append(current_sandwich)
    print("\n")
    print("Here are the sandwiches we made for you:")
    for sandwich in finished_sandwiches:
        print(f"- {sandwich}")
else:
    print("Your order is empty.")
