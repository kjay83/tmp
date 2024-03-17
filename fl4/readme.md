#simple project get numero ticket congo telecom
#un ticket est compose de la categorie sur 2 lettres max + delimiteur (-) + numero de sequence sur 4 chiffres
#Chaque num de sequence est specifique a chaque categorie chaque nom de categorie est unique
#et chaque num de ticket genere est par consequent unique
# Exemple: R-120 =categorie Reclamation sequence 120
#quand un ticket est imprime/ ou son numero confirme, 
#le prochain ticket incremente les sequences d'un pas (valeur par defaut=1)

#Objectif de l'api: generer num de ticket
#objectif de l'appli web : plus tard faire une page web pour recup et gerer les num de ticket
#il s'agira alors de simuler le comportement d'une borne physique en banque où un client 
#selectionne 1 bouton de categorie, la borne imprime le ticket avec le numero
# un ecran affiche que le ticket XX est attendu au guichet Z, pris en charge, traité etc...

#api details
#GET /newtickets/status : renvoie la liste des categories existantes avec toutes leurs valeurs
#GET /newtickets : renvoie un nouveau ticket avec categ par defaut, incremente la sequence pour preparer le prochain ticket
#GET /newtickets?name="AJ" : recupere un nouveau ticket pour la categorie specifiee. incremente la sequence pour preparer le prochain ticket. Renvoi 404 si la categorie n'existe pas (pas de sequence existante)  
#POST /newtickets?name="AJ"&sequence=45&increment=3&description="" : cree la nouvelle categorie. Renvoie 404 si existe deja 
#PUT /newtickets?name="AJ"&sequence=45&increment=3&description="" : modifie les valeurs de la categorie 
#Renvoi 404 si la categ n'existe pas. Si le param est vide, ne modifie rien
#DELETE /newtickets?name="AJ" : supprime la categorie specifiée et sa sequence associée
