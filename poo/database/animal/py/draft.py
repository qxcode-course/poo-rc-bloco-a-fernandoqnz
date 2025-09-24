class Animal():
    def __init__(self, species: str, sound: str, age:int):
        self.species:str=species
        self.sound:str=sound
        self.age:int=0


    def ageBy(self, amount:int):
        self.age+=4 
        
    