import csv
import random

class Astronaut:
    def __init__(self,name,flighthrs,status):
        self.name = name
        self.flighthrs = flighthrs
        self.status = status
    
    def __gt__(self,other):
        if self.flighthrs > other.flighthrs:
            return True
        return False
        
    def __ge__(self,other):
        if self.flighthrs >= other.flighthrs:
            return True
        return False
        
    def __eq__(self,other):
        if self.flighthrs == other.flighthrs:
            return True
        return False
        
    def __str__(self):
        return f"{self.name}, {self.status}"
        
f = open("astronauts.csv")
csvreader = csv.reader(f)
next(csvreader)     #skip the header row of the csv file
astronaut_lst = []
for i in csvreader:
    astro = Astronaut(i[0],int(i[13]),i[3])
    astronaut_lst.append(astro)
    
print(f"Name: {astronaut_lst[0].name}\nFlight Hours: {astronaut_lst[0].flighthrs}\nStatus: {astronaut_lst[0].status}")

astro1 = random.choice(astronaut_lst)
astro2 = random.choice(astronaut_lst)
print(f"{astro1.name} has more flight hours than {astro2.name}: {astro1 > astro2}")

for i in astronaut_lst:
    print(i)
    
f.close()