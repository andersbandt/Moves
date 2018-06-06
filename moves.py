import datetime

class Move():
    
    def __init__(self,name,start,end,location,money,date):
        # declares all of the attributes for a Move object
        self.name = name
        self.start = start
        self.end = end
        #self.date = 
        self.location = location
        self.money = money
        self.date = date

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
    
    def isLocation(location):
        if (location == "A"):
            return true
        if (self.location == location):
            return true
        else:
            return false
    
    def isMoney(money):
        if (self.money <= money):
            return true
        else:
            return false
        
    def isDay(day):
        if (self.day == 1):
            return true
        if (self.day == day):
            return true
        else:
            return true

rockets = []
rockets.append(Move("Insomnia Cookies", 9, 3, "Minneapolis", 6,1))
rockets.append(Move("$2 Bowling", 21.5, 1, "Arden Hills", 2,"Monday"))
rockets.append(Move("$2 Bowling", 21.5, 1, "Arden Hills", 2,"Sunday"))
rockets.append(Move("$2 Bowling", 21.5, 1, "Arden Hills", 2,"Wednesday"))
rockets.append(Move("$2 Bowling", 21.5, 1, "Arden Hills", 2,"Thursday"))
rockets.append(Move("Bowling", 11, 1, "Arden Hills", 6,1 ))
rockets.append(Move("Canoe/Kayak", 8, 19, "A" , 0,1))
rockets.append(Move("Hiking", 8, 19, "A", 0,1))
rockets.append(Move("Beach", 8, 19, "A", 0,1))
rockets.append(Move("Bridge Jumping", 8, 19, "Shoreview", 0,1))
rockets.append(Move("Bike Ride", 8, 19, "A", 0,1))
rockets.append(Move("Stone Arch Bridge Festival", 0, 0, "Minneapolis", 10, "6/15"))
rockets.append(Move("Stone Arch Bridge Festival", 0, 0, "Minneapolis", 10, "6/16"))
rockets.append(Move("Stone Arch Bridge Festival", 0, 0, "Minneapolis", 10, "6/17"))
rockets.append(Move("Movie", 0, 0, "A", 13, 1))
rockets.append(Move("Rozies' House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Ders' House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Luke's House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("James' Boat?", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Rozies' House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Minneapolis Institute of Art", 10, 17, "Minneapolis", 0,"Saturday"))
rockets.append(Move("Minneapolis Institute of Art", 11, 17, "Minneapolis", 0,"Sunday"))

realities = []

print("Please enter the following: time, location, date, money")
answer_time = input("What is the time? ")
answer_location = input("What is the location? ")
answer_date = input("What is the date? ")
answer_money = input("How much money? ")
for move in rockets:
    if ((move.isTime(answer_time) == true) and (move.isLocation(answer_location) == true) and (move.isMoney(answer_money) == money)):
        realities.append(move)
    
#prints all of the possibilities
for move in realities:
    print(move.name)



