name = 'unknown'

def intro():
    name = input("Who are you? ")
    welcome(name)

def welcome(name):
    print("Welcome, " + name)

# driver
intro()

