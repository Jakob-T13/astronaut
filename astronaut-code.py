import csv

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
    
print(str(astronaut_lst[0]))