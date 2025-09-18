class Towel:
    def __init__(self, color:str, size:str):
        self.color:str=color
        self.size:str=size
        self.wetness:int=0


#refencias 
print( "qual a cor da sua toalha")
color=input()
towel: Towel= Towel(color,"P")
print(f" a cor da sua toalha é:{towel.color}")
        
         
