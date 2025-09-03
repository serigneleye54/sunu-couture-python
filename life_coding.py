#1
def bonjour(prenon):
    print("bonjour",prenon)
#2    
    def ma_fonction(liste_nombre):
        liste_nombre = [1,2,3]
        somme = sum(liste_nombre)
        print("somme")
#3        
mes_prenoms=[]
for i in range (3):
    prenoms = input(f"Entrez les {i+1}prenoms:")
    prenoms.append(prenoms) 
    
#4 ecrir une fonction qui sauvegarde une liste de commande dans un fichier json 

import json
commandes={}
commandes.json={}
def sauvegarde(): 
    try:
        with open('commandes.json','r',encoding="utf-8") as f : 
           cmd = json.load(f)
           cmd = commandes
        with open('commandes.json','w',encoding="utf-8") as f : 
            json.dump(cmd,f,indent=4,ensure_ascii=False)
            print("commandes valides")
    except FileNotFoundError:
        print("erreur")