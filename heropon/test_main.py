from Perso import Perso 
import json

DEFAULTS_PARAMS = {}
with open("defaults.json",'r') as f:
    DEFAULTS_PARAMS = json.load(f)

def test_new_character_initial_values():
    #create new character
    #check initial values are setted
    t_name="Hero"
    t_health=12
    t_damage=11
    c1 = Perso(name=t_name,health=t_health,damage=t_damage)
    assert c1.name == t_name
    assert c1.health == t_health
    assert c1.damage == t_damage
    assert c1.maxHealth == 100

    # test new character default value if name is empty
    c2= Perso(name="",health=7000,damage=t_damage)
    assert c2.name == ""
    #test health is set to maxhEALTH if value is TOO BIG
    assert c2.health == c2.maxHealth

def test_character_attack():
    #when a character attack an other, the one who receive attack
    # get his heath diminished by damage from attacker
    c1 = Perso(name="A",health=10,damage=2)
    c2health=50
    c2 = Perso(name="B",health=c2health,damage=5)
    c1.attack(c2)
    assert c2.health == c2health-c1.damage

    #check that health doesnt go negative
    c3 = Perso( name="C",health=10,damage=1500)
    c3.attack(c1)
    assert c1.health == 0
    