import time
from datetime import datetime





class chrono :
    def __init__(self):
        self.datetime = 0
        self.start = 0
        self.end = 0

    def demarrer( self):
        self.datetime = datetime.today()
        self.start = time.perf_counter()
    
    def donner_chrono(self):
        if self.start == 0:
            return 0
        elif self.end != 0:
            return self.end - self.start
        else :
            return int(time.perf_counter() - self.start )     

    def stopper (self):
        self.end = time.perf_counter()


class sablier :
    def __init__(self, temps):
        self.temps_initial = temps
        self.temps = temps
        self.started = False
        self.datetime = 0
        self.start = 0
        self.end = 0
        self.temps_restant = temps


    def demarrer( self):
        if not self.started :
            self.datetime = datetime.today()
            self.start = time.perf_counter()
        self.started = True

    def donner_temps_restant(self):
        if self.started : 
            self.temps_restant = self.temps -int( time.perf_counter() - self.start)
            if self.temps_restant < 0 :
                self.temps_restant = 0
        return self.temps_restant
    
    def redemarrer(self) : 
        self.temps = self.temps_initial
        self.started = False
        self.datetime = 0
        self.start = 0
        self.end = 0
        self.temps_restant = self.temps
        
    

