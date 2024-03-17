from typing import Self

class Perso:    
    def __init__(self, name : str ="NEW", 
                 health:int =100, 
                 maxHealth:int =100 ,
                 damage:int=1):        
             
        self.name = name
        self.maxHealth=maxHealth
        self.health = health
        if (health>self.maxHealth):
            self.health = self.maxHealth
        self.damage= damage
    
    def attack(self,target:Self) -> None:
        target.health -= self.damage
        #if negative, health is 0
        target.health=max(0,target.health)
        print(f"{self.name.capitalize()} attacks {target.name.upper()} : (- {self.damage})")
        if target.health==0:
            print(f"{target.name} has no more HP.")
        
