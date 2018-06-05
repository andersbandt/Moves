class Move():
    
    def __init__(self,name,start,end,location,money):
        # declares all of the attributes for a Move object
        self.name = name
        self.start = start
        self.end = end
        #self.date = 
        self.location = location
        self.money = money

    def time(self):
        return self.start
        



rockets = []
rockets.append(Move("Insomnia Cookies", 9, 3, "Minneapolis", 6))
rockets.append(Move("Bowling", 21.5, 1, "Arden Hills", 6))
rockets.append(Move("Canoe/Kayak", 8, 19, "A" , 0))
rockets.append(Move("Hiking", 8, 19, "A", 0))
rockets.append(Move("Beach", 8, 19, "A", 0))
rockets.append(Move("Bridge Jumping", 8, 19, "Shoreview", 0))
rockets.append(Move("Bike Ride", 8, 19, "A", 0))
rockets.append(Move("Stone Arch Bridge Festival", 0, 0, "Minneapolis", 10))
rockets.append(Move("Movie", 0, 0, "A", 13))




realities = []





time = input("What time are you looking for?")
location = raw_input("Any particular location?")
money = input("What is your money cap?")



for move in rockets:
    if (move.end - move.start > 0):
        if (move.end > time and move.start < time):
            realities.append(move)
#tests to see if there is no required time            
    elif (move.end == 0 and move.start == 0):
            realities.append(move)
    else:
        if (time < move.end or time > move.start):
            realities.append(move)







#prints all of the possibilities
for move in realities:
    print(move.name)
