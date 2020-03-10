name = 'unknown'

def intro():
    name = input("Who are you? ")
    welcome(name)

def class():
    global name
    print("Hey " + name + ", welcome to the family")

def welcome(name):
    print("Welcome, " + name)

# driver
intro()

