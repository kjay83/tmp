class Healthbar:
    def __init__(self,currenthp:int = 100, maxhp:int = 100,name_to_show:str = "PERSO", show_name:bool = False) -> None:
        self.currenthp=currenthp
        self.maxhp=maxhp
        self.symbol_barrier_out=']'
        self.symbol_barrier_in='['
        self.symbol_hp='/'
        self.symbol_empty='_'
        self.current_hp_bar=''
        self.remaining_hp_bar=''
        self.final_hpbar=''
        self.name_to_show=name_to_show
        self.show_name=show_name
        self.generateBar()

    def generateBar(self)->None:
        nb_current_hp_bar=round((self.currenthp/self.maxhp)*10)
        nb_remaining_hp_bar=round(((self.maxhp-self.currenthp)/self.maxhp)*10)
        self.current_hp_bar = nb_current_hp_bar*self.symbol_hp
        self.remaining_hp_bar = nb_remaining_hp_bar*self.symbol_empty
        self.final_hpbar = \
            f"{self.symbol_barrier_in}{self.current_hp_bar}{self.remaining_hp_bar}{self.symbol_barrier_out}"

    def update(self,currenthp:int)-> None:
        if currenthp>self.maxhp:
            currenthp=self.maxhp
        if currenthp<0:
            currenthp=0
        self.currenthp=currenthp
        self.generateBar()
        

    def draw(self):
        result=""
        if self.show_name:
            result+=f"{self.name_to_show} : "
        result+=f"HP {self.currenthp}/{self.maxhp} {self.final_hpbar} "
        print(result)

if __name__ == "__main__":
    # h = Healthbar(57,100,"",True)
    h = Healthbar(currenthp=157,maxhp=300,show_name=True)
    h.draw()
    print("updating...")
    h.update(100)
    h.draw()