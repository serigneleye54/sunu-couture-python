import re
import datetime
import json
#creation de liste commande :
#definition du dictionnaire :

def  saisir_commande() :
    client = {}
    #ajout d'un tuple pour recuperer la valeur des variable:
    nom,prenom,telephone,email,sexe,vetement,taille,hanche,longueur,livraison,retouche = ajouter_commande()
    
    #creation du dictionnaire commande :       
    commande = {
        "nom" : nom,
        "prenom" : prenom,
        "telephone" : telephone,
        "email" : email,
        "sexe" : sexe,
        "vetement" : vetement,
        "taille" : taille,
        "hanche" : hanche,
        "longueur" : longueur,
        "retouche" : livraison,
        "livraison" : retouche,
        }
    commandes = {
     
        "nom" : "",
        "prenom" : "",
        "telephone" : "",
        "email" : "",
        "sexe" : "",
        "vetement" : "",
        "taille" : "",
        "hanche" : "",
        "longueur" : "",
        "retouche" : "",
        "livraison" : "",
        
    }
    
    #creation de la fonction afficher commande:
    print("\nMes commandes:")
    items = list(commandes.items())
    for i in range(len(items)):
        print(f"commande {i}:")
        print(f"nom:{items[i][1]}")
        print(f"prenom:{items[i][2]}")
        print(f"telephone:{items[i][3]}")
        print(f"email:{items[i][4]}")
        print(f"hanche:{items[i][5]}")
        print(f"longueur:{items[i][6]}")
        print(f"retouche :{items[i][7]}")
        print(f"livraison:{items[i][8]}")
    #chargement des commandes.
    try:
        #on a dit au programme douvrir le fichier(commandes.json) et de faire la lecture (r)
        with open('commandes.json','r') as fichier:
            commandes = json.load(fichier)
        print("commande chargée avec success!.")
    except FileNotFoundError:
        print("Aucun fichier de commande trouvé.")
        commandes = []
    #ajout du dictionnaire a la liste commande:
    commandes.append(commande)
    print("\nCommande ajoutée avec succes.")
    
            
    #Sauvegarder toutes les commandes dans un fichier commandes.json à la fin
    #on a dit au programme douvrir le fichier(commandes.json) et décrire la commande
    with open('commandes.json','w') as fichier:  
        json.dump(commandes,fichier,indent=4)  
        print("\nCommande sauvegardée avec succés !") 
         
           
            
   
    client = {
        "options": {
           
            "commentaire": input("Veuillez laisser un commentaire : "),
        }
    }        
            
    
            
    date_du_jour = datetime.date.today().strftime("%d/%m/%Y")
    print(f"Date de la commande:{date_du_jour}")   
    
        
    #ajouter une commande:
    print("\nAjout d'une nouvelle commande")
    while True:
        reponse = input("Voulez vous ajoutez une nouvelle commande:")
        if  reponse.lower() == "oui":
            numero = input("Entrez le numero de la commande:")
            description = input("Entrez la description de la commande:")
            commandes.append({"numero":numero,"description":description})
            print("Commande ajoutée avec succés.")
            break
        elif reponse.lower()=="non":
            print("Ajout de commande annulé.")
            break
        else:
            print("Reponse invalide.Veullez répondre par oui ou non.")
           
    #affichage de toutes les commandes:
    if not commandes:
        print("Aucune commande n'a été ajoutée.")
    else:
        for i,commande in enumerate(commandes,start=1):
            if 'nom' in commande and 'description' in commande:
                print(f"{i}.{commande['nom']} - {commande['description']}")
                
        
    #statistique sur les commandes:
    if not commandes:
        print("Aucune commande n'a été ajoutée.")
    else:
        print(f"\nNombre de commandes : {len(commandes)}")
        
        
    #Rechercher une commande par numero:
    numero = input("\nNumero de la commande a rechercher :")
    for commande in commandes:
        if 'numero' in commande and commande["numero"] == numero:
            if' description 'in commande:
                print(f"commande trouvée : {commande['numero']} -{commande['description']}")
            else:
                print(f"commande trouvée : {commande['numero']}")
    
    
def ajouter_commande():
    #initialisation des variables
    nom = ""
    prenom = ""
    telephone =""
    email = ""
    vetement = ""
    sexe = ""
    taille = ""
    hanche = ""
    longueur = ""
    livraison = ""
    retouche = ""
    while True:
        print("Formulaire de commande:")
        nom = input("Entrez le nom : ")
        if  nom == False :
            print("Ce champ est requis.")
        elif nom.isdigit():
            print("Les lettres sont seulements autorisées")
        else: 
            
            break
        
    
    while True:
        prenom= input("Entrez le prenom: ")
        if prenom == False :
            print("Ce champ est requis.")
        elif prenom.isdigit():
            print("Les lettres sont seulements autorisées")
        else:
            
            break
        
    
    while True:
        telephone= input("Entrer le numéro de téléphone:")
        if telephone == False :
            print("Ce champ est requis.")
        elif telephone.isalpha():
             print("Les chiffres sont seulements autorisées")
        else:
            
            break 
        
    
    while True:
        email= input("Entrer l'adresse email:")
        if not email:
            print("Ce champ est requis.")
        elif email == False:
            print("Veuillez saisir un email valide.")
        else:
            
            break
        
        
    vetements= ["robe","costume","chemise","jean"]
    while True:
        vetement = input("Entrer le type de vetement choisi(robe,costume,chemise,jean):").lower()
        if vetement == False:
            print("Ce champ est requis.")
        elif vetement in vetements:
            #concaténation avec +
            print("Vous avez choisi: " + vetement)
            break
        else:
            print("Type de vetement non valide.veullez resaisir un type de vetement dans la liste.")
    
            
      
    liste_sexe = ["homme","femme"]
    while True:
        sexe = input("Entrer le type de sexe(homme/femme):").lower()
        if sexe == False:
            print("Ce champ est requis.")
        elif sexe in liste_sexe :
            #concaténation avec f
            print(f"Vous etes un(e):{sexe}")
            break
        else:
            print("Invalide.Veuillez saisir homme ou femme:")
    
            
    
    while True:
        try:
            taille = float(input("Veuillez saisir la taille:"))
            if taille != 0:
                break
            else:
                print("Taille doit etre strictement superieur a zero.")
        except ValueError:
            print("Taille doit etre un nombre.")
            
    while True:
        try:
            hanche = float(input("Veuillez saisir hanche:"))
            if hanche != 0:
                break
            else:
                print("Hanche doit etre strictement superieur a zero.")
        except ValueError:
            print("Hanche doit etre un nombre.")
             
    while True:        
        try:
            longueur = float(input("Veuillez saisir la longueur:"))
            if longueur != 0:
                break
            else:
                print("Longueur doit etre strictement superieur a zero.")
        except ValueError:
            print("Longueur doit etre un nombre.")
              
    
           
    choix = ["oui","non"]
    while True:
        livraison = input("Entrez oui ou non pour livraison:").lower()  
        if livraison in choix:
            print(f"Vous avez choisi :{livraison}")
            break
        else:
            print("Choix non valide")
    
            
    choix = ["oui","non"]
    while True:
        retouche = input("Entrez oui ou non pour retouche:").lower()  
        if retouche in choix:
            print(f"Vous avez choisi :{retouche}")
            break
        else:
            print("Choix non valide")
    #renvoi des variables
    return nom,prenom,telephone,email,vetement,sexe,taille,hanche,longueur,livraison,retouche  
    
             
def valider_nom(nom):
    if not nom:
        return False
    else:
        return True
    
def valider_prenom(prenom):
    #verifie si le champ prenom est vide
    if not prenom:
        return False
    else:
        return True
    
def valider_numero(telephone):
    if not telephone:
        return False
    else:
        return True
    #importation de re(regular expression)patern de caractere qui permettent de rechercher,de valider
    # et de manipuler des chaines de caracteres.

def valider_email(email):
    #^ :le debut de la chaine.
    #[a-zA-Z0-9_.+-]+ :un ou plusieur caracteres alphanumeriques,point,tirets-bas,plus ou tirets.
    #. : le point echapé avec un antislash qui a une signification special en regex.
    #$ : la fin de la chaine.
    patern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    #verification si l'adresse email correspond a ce patern,la fonction retourne true sinon elle retourne false.
    if re.match(patern, email):
        return True
    else:
        return False
    
    
def valider_vetement(vetement):
    if not vetement:
        return False
    else:
        return True
    
    
def valider_sexe(sexe):
    if not sexe:
        return False
    else:
        return True
    
def valider_mesure(mesure):
    if not mesure:
        return False
    else:
        return True
    
def valider_option(option):
    if not option:
        return False
    else:
        return True
    
    
def afficher_commande(commande):
    if not commande:
        return False
    else:
        return True
    

    
def sauvegarder_commande(commande):
    if not commande:
        return False
    else:
        return True
    
        
def charger_commande(commande):
    if not commande:
        return False
    else:
        return True 
    
def calcul_moyenne_mesures(commande): 
    if not commande:
        return None  

def taille_recommandee(mesure):
    if not taille_recommandee:
        return False
    else:
        return True
    
def mesures(mesures):
    if not mesures:
        return False
    else:
        return True
    
def statistique_commande(commande):

    if not commande:
        return False
    else:
        return True 
    
def rechercher_commande(commande):
    if not commande:
        return False
    else:
        return True 
    
saisir_commande()
afficher_commande()