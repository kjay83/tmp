import datetime
import os
import json
from json import JSONEncoder


def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


class Job:
    def __init__(self, name, earnings, prerequisites):
        self.name = name.upper()
        self.earnings = earnings
        self.prerequisites = prerequisites

    def __str__(self):
        return f"{self.name} - [{self.earnings:,.2f} XAF/{g.units}]"

    def get_complete_job_details(self):
        return self.__str__() + f" - PREREQ= {self.prerequisites:,.2f} XAF"


class Game:
    def __init__(self):
        self.nb_tour = 0
        self.speed = 1
        self.cash = 0
        self.earnings_from_start = 0
        self.total_cash_flows = 0
        self.units = "Hour"
        self.jobs_dictionnary = {
            "SDF": Job("SDF", 0, 0),
            "CONSTRUCTION": Job("CONSTRUCTION", 10000, 0),
            "DELIVERY": Job("DELIVERY", 15000, 50000),
            "WAITER": Job("WAITER", 20000, 70000),
            "SECRETARY": Job("SECRETARY", 70000, 100000),
            "DRIVER": Job("DRIVER", 90000, 150000),
            "COMPTABLE": Job("COMPTABLE", 200000, 300000),
        }
        self.jobs_list_names = list(self.jobs_dictionnary)
        self.work_position = self.jobs_dictionnary[self.jobs_list_names[0]]
        self.filename = "revdiv.json"

    def init_from_dict(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])


class GameEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


g = Game()


def show_datas():
    print('*' * 30)
    print(f"ROUND N° {g.nb_tour}")
    print(f"Game Speed : {g.speed} {g.units}/ Tour")
    print(f"Your work position : {g.work_position}")
    print(f"Your total actual Cash flow: {g.total_cash_flows:+,.2f} XAF /{g.units}")
    print(f"(Stats: Since 1rst turn, you generated: {g.earnings_from_start:+,.2f} XAF )")
    print(f"-" * 20)
    print(f"CASH: {g.cash:,.2f} XAF")
    print(f"-" * 20)
    print('*' * 30)


def update_total_earnings():
    g.total_cash_flows = g.work_position.earnings


def user_choose_job(job_id):
    job_name = g.jobs_list_names[job_id]
    g.work_position = g.jobs_dictionnary.get(job_name)
    update_total_earnings()
    g.cash -= g.work_position.prerequisites


def show_work_menu():
    clear_screen()
    print(f"-" * 20)
    print(f"WORK MENU")
    print(f"-" * 20)
    print(f"Vous disposez de {g.cash:,.2f} XAF.")
    print(f"Vous êtes actuellement {g.work_position}. Voici les autres jobs disponibles:")
    print(f"Legende: (NUMERO)- JOB - [REVENUS] - PRE REQUIS")

    for i in range(len(g.jobs_list_names)):
        job_position = g.jobs_dictionnary.get(g.jobs_list_names[i])
        print(f"({i + 1}) - {job_position.get_complete_job_details()}")

    print(f"0- Revenir à l'ecran général")
    print(f"-" * 20)


def save_game_data():
    print("saving...")
    with open(g.filename, 'w') as f:
        data_json = json.dumps(g, ensure_ascii=True, indent=4, cls=GameEncoder)
        f.write(data_json)
    input("saving done successfully>> ")


def load_game_data():
    print("loading datas...")
    with open(g.filename, 'r') as f:
        data_json = f.read()
    data = json.loads(data_json)
    print(f"type data {type(data)} and data are : {data}")
    g2 = Game()
    g2.init_from_dict(data)
    #print(f"type g2 {type(g2)} and are : {g2.cash} and {g2.work_position} and {g2.jobs_dictionnary}")

    g.cash = g2.cash
    g.earnings_from_start = g2.earnings_from_start
    g.work_position = Job(g2.work_position.get("name"),g2.work_position.get("earnings"),g2.work_position.get("prerequisites"))

    g.speed = g2.speed
    g.nb_tour = g2.nb_tour
    g.total_cash_flows = g2.total_cash_flows

    # NON TRAITE CAR NON MODIFIE AU COURS DU JEU...
    #g.jobs_dictionnary = g2.jobs_dictionnary
    #g.units = g2.units
    #g.filename = g2.filename
    #g.jobs_list_names = g2.jobs_list_names
    input("data loaded sucessfully! >> ")



def get_save_load_choice():
    clear_screen()
    print(f"-" * 5 + f"SAVE/LOAD SCREEN" + f"-" * 5)
    answer = input(f"(1) - SAVE | (2) - LOAD | (0) - ANNULER >>> ")
    while not answer.isnumeric():
        answer = input(f"Please retry!! \n (1) - SAVE | (2) - LOAD | (0) - ANNULER >>> ")
    answer_num = int(answer)
    choice_done = False
    while not choice_done:
        if answer_num in range(0, 3):
            choice_done = True
            match answer_num:
                case 0:
                    print("exiting LOAD/SAVE menu.")
                case 1:
                    save_game_data()
                case 2:
                    load_game_data()
        else:
            # TODO: what if it is a string
            answer_num = int(input("Veuiller saisir un nombre entre 0 et 2. >>> "))


def get_work_menu_choice():
    jobs_number = len(g.jobs_list_names)
    choice_done = False
    while not choice_done:
        show_work_menu()
        answer = input(f"Merci d'indiquer votre choix : ")
        while not answer.isnumeric():
            answer = input(f"Merci d'indiquer votre choix : ")

        job_choosen = int(answer)
        if (job_choosen > len(g.jobs_list_names) or job_choosen < 0):
            print(f"/!\\ Merci d'entrer un chiffre entre 0 et {jobs_number}.")
            input("Appuyer sur ENTREE pour continuer")
        else:
            temp_job = g.jobs_dictionnary.get(g.jobs_list_names[job_choosen - 1])
            if temp_job.name == g.work_position.name:
                input(f"Vous occupez DEJA ce poste ({g.work_position}). Appuyer sur ENTREE svp")
            elif g.cash >= temp_job.prerequisites:
                user_choose_job(job_choosen - 1)
                choice_done = True
                print(f"Une somme de {g.work_position.prerequisites:,.2f} XAF a été prélevée.")
                input(f"Felicitations pour votre nouvelle position de {g.work_position}! Appuyer sur ENTREE svp")
            else:
                input(
                    f"Vous avez besoin de {temp_job.prerequisites:,.2f} XAF dans votre compte pour ce job de {temp_job.name}. [vous avez {g.cash:,.2f} XAF]")
                # input("Appuyer sur ENTREE pour continuer")


def show_general_menu():
    clear_screen()
    show_datas()


def game_next_turn():
    added_cash = g.total_cash_flows * g.speed
    g.cash += added_cash
    g.earnings_from_start += added_cash
    g.nb_tour += 1


def get_general_menu_choice():
    error_msg = f"/!\\ Merci d'entrer un chiffre entre 0 et 1!! /!\\"
    while True:
        clear_screen()
        show_general_menu()
        print(f"Que désirez-vous faire ? ")
        print(f"(ENTREE) - Next Round | (1) - JOBS | (9) - SAVE/LOAD | (0) - QUITTER")
        answer = input(f"Merci d'indiquer votre choix : ")
        if answer.isspace():
            game_next_turn()
        elif (answer.isnumeric()):
            answer2 = int(answer)
            match answer2:
                case 1:
                    get_work_menu_choice()
                case 9:
                    get_save_load_choice()
                case 0:
                    exit_game_with_message()
                case _:
                    print(error_msg)
                    input("Appuyer sur ENTREE pour continuer")
        else:
            game_next_turn()


def exit_game_with_message():
    print("=============================================================================")
    print(f"Vous avez fini le jeu au bout de {g.nb_tour} {g.units}(s) et un patrimoine de: {g.cash:,.2f} XAF")
    exit()


def game_start():
    print(f"starting game showing datas")
    g.work_position = g.jobs_dictionnary["WAITER"]
    show_datas()
    input("Appuyer sur ENTREE pour continuer")
    str1 = "start"
    g.total_cash_flows += g.work_position.earnings
    while str1.upper() != 'Q':
        g.cash += g.total_cash_flows * g.speed
        g.nb_tour += g.speed
        show_datas()
        str1 = input("Appuyer sur ENTREE pour continuer ou saisir 'Q' pour quitter")

    print("=============================================================================")
    print(f"Vous avez fini le jeu au bout de {g.nb_tour} {g.units}(s) et un patrimoine de: {g.cash:,.2f} XAF")
    exit()


if __name__ == '__main__':
    # game_start()
    # show_work_menu()
    # get_work_menu_choice()
    # print("after get wor kcoice")
    # show_datas()
    get_general_menu_choice()
