
# Defining the cost of each USB stick
cost_per_stick = 6

# Defining the amount of money available
money_available = 50

# Calculating the number of USB sticks that can be purchased
number_of_sticks = money_available // cost_per_stick

# Calculating the remaining amount of money
remaining_money = money_available % cost_per_stick

# Printing the number of USB sticks that can be purchased and the remaining amount of money
print("Number of USB sticks:", number_of_sticks)
print("Remaining amount of money: £" + str(remaining_money))
