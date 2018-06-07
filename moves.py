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

    def isTime(self, time):
        if (self.end - self.start > 0):
            if (self.end > time and self.start < time):
                return True
#tests to see if there is no required time            
        elif (self.end == 0 and self.start == 0):
            return True
        else:
            if (time < move.end or time > move.start):
                return True
        return False
    
    def isLocation(self, location):
        if (location == "A"):
            return True
        if (self.location == location):
            return True
        else:
            return False
    
    def isMoney(self, money):
        if (self.money <= money):
            return True
        else:
            return False
        
    def isDate(self, date):
        if (self.date == 1):
            return True
        if (self.date == date):
            return True
        else:
            return False

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
rockets.append(Move("Stone Arch Bridge Festival", 0, 0, "Minneapolis", 10, 6.15))
rockets.append(Move("Stone Arch Bridge Festival", 0, 0, "Minneapolis", 10, 6.16))
rockets.append(Move("Stone Arch Bridge Festival", 0, 0, "Minneapolis", 10, 6.17))
rockets.append(Move("Movie", 0, 0, "A", 13, 1))
rockets.append(Move("Rozies' House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Ders' House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Luke's House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("James' Boat?", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Rozies' House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Mitch's House", 0, 0, "Shoreview", 0,1))
rockets.append(Move("Minneapolis Institute of Art", 10, 17, "Minneapolis", 0,"Saturday"))
rockets.append(Move("Minneapolis Institute of Art", 11, 17, "Minneapolis", 0,"Sunday"))
rockets.append(Move("Velodrome Bike Racing", 7, 8, "Blaine", 0,"Thursday"))
rockets.append(Move("Cowboy Jack's 2 Dollar Burgers", 4, 10, "Shoreview", 2,"Wednesday"))
rockets.append(Move("Movie in a Park- Moana", 9, 11, "A", 2,"6/23"))
rockets.append(Move("Movie in a Park- Wonder woman", 9, 11, "A", 2,6.25))
rockets.append(Move("Movie in a Park- Lego Batman Movie", 9, 11, "A", 2,6.30))
rockets.append(Move("Movie in a Park- Spider- Homecoming", 9, 11, "A", 2,"7/5"))
rockets.append(Move("Movie in a Park- Incredibles", 9, 11, "A", 2,"7/20"))
rockets.append(Move("Movie in a Park- Ferris Bueller's Day Off", 9, 11, "A", 2,"7/21"))
rockets.append(Move("Movie in a Park- ", 9, 11, "A", 2,""))
rockets.append(Move("Fuck it- Kyoto?", 8, 10.5, "A", 30,1))



realities = []

print("Please enter the following: time, location, date, money")
answer_time = input("What is the time? ")
answer_location = raw_input("What is the location? ")
answer_date = raw_input("What is the date? ")
answer_money = input("How much money? ")
for move in rockets:
    if ((move.isTime(answer_time) == True) and (move.isLocation(answer_location) == True) and (move.isMoney(answer_money) == True) and (move.isDate(answer_date) == True)):
        realities.append(move)
    
#prints all of the possibilities
for move in realities:
    print(move.name)

