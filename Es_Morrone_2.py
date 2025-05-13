import math

class Pagella:
    def __init__(self, voti):
        self.voti = voti

    def __repr__(self):
        return self.voti

    def media(self):
        if len(self.voti) == 0:
            return 0
        return sum(self.voti) / len(self.voti)

    def __getitem__(self, i):
        return self.voti[i]

    #def __eq__(self):


    def __sub__(self, other):
        if len(self.voti) !=  len(other.voti):
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate")
            return None
        

        