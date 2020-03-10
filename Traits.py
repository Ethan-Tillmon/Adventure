class traits(objects):
    race = ["black", "caucasian", "hispanic", "asian", "middle eastern"]
    height = ["6'03", "6'02", "6", "5'11", "5'10", "5'09", "5'08"]
    skincolor = ["black", "light black", "brown", "light brown", "tan", "white"]
    haircolor = ["brunette", "blond", "dirty blond", "red"]
    pensize = ["big", "average", "micro"]

    def __init__(self,name,race,height,skincolor,haircolor,pensize):
        self.name = name
        self.race = race
        self.height = height
        self.skincolor = skincolor
        self.haircolor = haircolor
        self.pensize = pensize

    def chooseRace(self):
        self.race = input("What race is your character? Pick your number."
            "Black: 1"
            "Caucasion: 2"
            "Hispanic: 3"
            "Asian: 4"
            "Middle eastern: 5"
            "Your race number: ")

    def __str__(self):
        if(race == 1):Black
            
    
    
