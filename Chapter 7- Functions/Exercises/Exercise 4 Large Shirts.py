#If no arguments are passed, the default values will be used
def make_shirt(size='small', message='Christian Dave Sicat'):

    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It is going to say, "{message}"')

#Call the function using the default values
make_shirt()

#Call the function with size='medium'
make_shirt(size='medium')

#Call the function with size='large' and a custom message
make_shirt('large', 'Christian Dave Sicat')