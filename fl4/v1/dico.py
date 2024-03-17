import json

eleves={
    'albert':18,
    'oscar':10,
    'classi':8
}
print(f"STARTING: {eleves.get('alberto','UNDEFINED')}")
for nom,note in eleves.items():
    print(f"Eleve {nom} : {note}")

moy = sum(eleves.values())/len(eleves.values())
print(f"La moyenne de la classe est de {moy}")

#recup from a file
with open('classe1.json','r+' ) as file:
    #json.dump(collegiens, file)
    collegiens=json.load(file)

#adding a collegiens
collegiens['Parm']={'note':18,'appreciation':"Excellent"}
collegiens.update({'NADIA':{'note':17,'appreciation':"not bad at all"}})
#print(collegiens['classi']['appreciation'])
for collegien,bulletin in collegiens.items():
    print(f"Eleve {collegien} : Note= {bulletin['note']} / Appreciation= {bulletin['appreciation']} ")
print("deleting oscar")
collegiens.pop('oscar')
#modify note de albert
collegiens['albert']['note']=20
print("new version")
for collegien,bulletin in collegiens.items():
    print(f"Eleve {collegien} : Note= {bulletin['note']} / Appreciation= {bulletin['appreciation']} ")

#save in a file
with open('classe2.json','w+' ) as file:
    json.dump(collegiens, file)