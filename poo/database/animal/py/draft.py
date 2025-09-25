class Animal():
    def __init__(self, species: str, sound: str):
        self.species:str=species
        self.sound:str=sound
        self.age:int=0


    def __str__(self) -> str:
        return (f"{self.species}:{self.age}:{self.sound} morreu.")
    
    def ageBy(self, increment:int):
        if self.age==4:
            return(f"{Warning:self.species} morreu.")
        
        self.age += increment
        if self.age >= 4:
            self.age = 4
            return(f"{Warning:self.species} morreu.")
            
    def makeSound(self):
        if self.age==0:
            return("---")
        if self.age==4:
            return("morreu.")
        return self.sound

        
    