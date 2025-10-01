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


def main():
    animal: Animal = Animal("", "")
    while True:

        line: str = input() # 4: perguntar ao usuario
        print("$" + line) # echo
        args: list[str] = line.split(" ") # 5: separar argumentos

        if args[0]== "end":
            break
        elif args[0]=="criar":
            species:  str=args[1]
            sound: str=args[2]
            age: str=args[3]
            animal= Animal(species, sound, age)

