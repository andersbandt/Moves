class Move():
    
    def __init__(self,name,start,end,location,money):
        # declares all of the attributes for a Move object
        self.name = name
        self.start = start
        self.end = end
        #self.date = 
        self.location = location
        self.money = money

    def isTime(time):
        if (end - time > 0):
            if (end > time and start < time):
                return true
#tests to see if there is no required time            
        elif (end == 0 and start == 0):
            return true
        else:
            if (time < move.end or time > move.start):
                return true
        return false


        



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

sort = raw_input("What do you want to sort by; time, location, date, money, or multiple?")
if (sort == "time"):
                 answer_time = input("What is the time?")
                 for move in rockets:
                    if (move.isTime(answer_time) == true):
                        realities.append(move)
                 
#prints all of the possibilities
for move in realities:
    print(move.name)



