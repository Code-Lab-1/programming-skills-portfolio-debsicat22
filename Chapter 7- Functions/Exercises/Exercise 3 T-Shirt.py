#Define a function named "make_shirt" that takes in two parameters, size and message
def make_shirt(size, message):

    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It is going to say, "{message}"')

#Call the function make_shirt with the arguments 'small'
make_shirt('small', 'Christian Dave Sicat')

#Call the function make_shirt with keyword arguments size='large'
make_shirt(message="Christian Dave Sicat.", size='large')