import json
# import typing
from Perso import Perso
from Healthbar import Healthbar

DEFAULTS_PARAMS = {}
with open("defaults.json",'r') as f:
    DEFAULTS_PARAMS = json.load(f)

class Game:
    default_params = {}
    hero : Perso
    ennemy : Perso
    continuegame : bool =True
    hero_healthbar : Healthbar    
    enemy_healthbar : Healthbar

    def __init__(self) -> None:
        with open("defaults.json",'r') as f:
            self.default_params = json.load(f)
        self.hero = Perso(name="HEROPON",
                          health=self.default_params.get("MAX_HEALTH"),
                          maxHealth=self.default_params.get("MAX_HEALTH"),
                          damage=self.default_params.get("DEFAULT_HERO_DAMAGE"))
        self.ennemy = Perso(name="HERONEMY",
                          health=self.default_params.get("MAX_HEALTH"),
                          maxHealth=self.default_params.get("MAX_HEALTH"),
                          damage=self.default_params.get("DEFAULT_DAMAGE"))
        
        self.hero_healthbar = Healthbar(self.hero.health,self.hero.maxHealth,self.hero.name,True)
        self.enemy_healthbar = Healthbar(self.ennemy.health,self.ennemy.maxHealth,self.ennemy.name,True)
    
    def intro(self) -> None:
        print("Welcome to the game.")
        print("Heropon will counter ennemies")
    
    def check_hero_dead(self) -> bool:
        if self.hero.health==0:
            print("Hero is dead, Game over!!")
            self.continuegame=False
            
    
    def check_enemy_dead(self) -> bool:
        if self.ennemy.health==0:
            print("Enemy is dead, YOU WON!!")
            self.continuegame=False

    def start(self) -> None:
        while (self.continuegame):
            self.hero_healthbar.draw()
            self.enemy_healthbar.draw()
            input("---Press enter to attack---")
            self.hero.attack(self.ennemy)
            self.enemy_healthbar.update(self.ennemy.health)
            self.hero_healthbar.update(self.hero.health)
            self.check_hero_dead()
            self.check_enemy_dead()
            