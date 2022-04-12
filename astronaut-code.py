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