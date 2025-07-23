import re
import datetime
import json
#creation de liste commande :
commandes = []
#definition du dictionnaire :
def  saisir_commande() :
    client = {}
    
    print("Entrez vos identifiants")
    while True:
        nom= input("Entrez le nom : ")
        if valider_nom(nom) == False :
            print("Ce champ est requis.")
        elif nom.isdigit():
            print("Les lettres sont seulements autorisées")
        else: 
            #ajouter un element dans un dictionnaire
            client["nom"] = nom
            break
        
    
    while True:
        prenom= input("Entrez le prenom: ")
        if valider_prenom(prenom) == False :
            print("Ce champ est requis.")
        elif prenom.isdigit():
            print("Les lettres sont seulements autorisées")
        else:
            client["prenom"] = prenom
            break
        
    
    while True:
        telephone= input("Entrer le numéro de téléphone:")
        if valider_numero(telephone) == False :
            print("Ce champ est requis.")
        elif telephone.isalpha():
             print("Les chiffres sont seulements autorisées")
        else:
            client ["téléphone"] = telephone
            break 
        
    
    while True:
        email= input("Entrer l'adresse email:")
        if not email:
            print("Ce champ est requis.")
        elif valider_email(email) == False:
            print("Veuillez saisir un email valide.")
        else:
            client ["email"] = email
            break
        
    print("\nType de vetement")    
    vetements= ["robe","costume","chemise","jean"]
    while True:
        vetement = input("Entrer le type de vetement choisi(robe,costume,chemise,jean):").lower()
        if valider_vetement(vetement) == False:
            print("Ce champ est requis.")
        elif vetement in vetements:
            #concaténation avec +
            print("Vous avez choisi: " + vetement)
            break
        else:
            print("Type de vetement non valide.veullez resaisir un type de vetement dans la liste.")
    
            
    print("\nSexe")  
    liste_sexe = ["homme","femme"]
    while True:
        sexe = input("Entrer le type de sexe(homme/femme):").lower()
        if valider_sexe(sexe) == False:
            print("Ce champ est requis.")
        elif sexe in liste_sexe :
            #concaténation avec f
            print(f"Vous etes un(e):{sexe}")
            break
        else:
            print("Invalide.Veuillez saisir homme ou femme:")
    
            
    print("\nVos mesures :")
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
            
    global commandes   
    nombre_commandes = len(commandes)
    #Initialise des variables pour sommer les tailles, hanches et longueurs.
    somme_tailles = 0
    somme_hanches = 0
    somme_longueurs = 0
    #Parcourt de chaque commande dans la liste.
    for commande in commandes:
        #Vérifie si la commande a le bon format (3 mesures). Si non, afficher commande invalide.
        if len(commande) != 3:
            print("Commande invalide")
            #Ajoute les mesures aux sommes respectives.
            somme_tailles += taille
            somme_hanches += hanche
            somme_longueurs += longueur
        #Calcule les moyennes en divisant les sommes par le nombre de commandes.
        if nombre_commandes == 0:
                print("Erreur")
        else:
            moyenne_tailles = somme_tailles / nombre_commandes
            moyenne_hanches = somme_hanches / nombre_commandes
            moyenne_longueurs = somme_longueurs / nombre_commandes
                
        #Fonction taille_recommandée(mesure) qui recommande un type de tissu ou 
        #coupe selon les valeurs.             
        mesures = {"taillle","hanche","longueur"}
        if taille is None or hanche is None or longueur is None:
           print("Les mesures sont incomplétes.")
        elif taille < 160:
           print("Vous avez une silhouette petite.Nous vous recommandons des coupes ajustées et des tissus légers.")
        elif taille >= 160 and taille <170:
            print("Vous avez une silhouette moyenne.Nous vous recommandons des coupes classiques et des tissus de qualité moyenne.")
        else:
            print("Vous avez une silhouette grande.Nous vous recommandons des coupes droites et des tissus épais.")
        
             
    print("\nVos options")        
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
    client = {
        "options": {
           
            "commentaire": input("Veuillez laisser un commentaire : "),
        }
    }        
            
    
            
    date_du_jour = datetime.date.today().strftime("%d/%m/%Y")
    print(f"Date de la commande:{date_du_jour}")   
    
    #creation du dictionnaire commande :
    commande = {
        "date" : date_du_jour,
        "taille" : taille,
        "hanche" : hanche,
        "longueur" : longueur,
        "retouche" : livraison,
        "livraison" : retouche,
        }
    #ajout du dictionnaire a la liste commande:
    commandes.append(commande)
    #creation de la fonction afficher commande:
    print("\nListe des commandes:")
    for i, commande in enumerate(commandes, start = 1):
        print(f"commande {i}:")
        print(f"date:{commande['date']}")
        print(f"taille:{commande['taille']}")
        print(f"hanche:{commande['hanche']}")
        print(f"longueur:{commande['longueur']}")
        print(f"retouche :{commande['livraison']}")
        print(f"livraison:{commande['retouche']}")
        
    #Sauvegarder toutes les commandes dans un fichier commandes.json à la fin
    #on a dit au programme douvrir le fichier(commandes.json) et décrire la commande
    with open('commandes.json','w') as fichier:  
        json.dump(commandes,fichier,indent=4)  
        print("\nCommande sauvegardée avec succés !") 
        
    #chargement des commandes.
    try:
        #on a dit au programme douvrir le fichier(commandes.json) et de faire la lecture (r)
        with open('commandes.json','r') as fichier:
            commandes = json.load(fichier)
        print("commande chargée avec success!.")
    except FileNotFoundError:
        print("Aucun fichier de commande trouvé.")
        
        
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
             
    print("\nMenu :")            
    while True:
        print("1.Ajouter une nouvelle commande")
        print("2.Afficher toutes les commande")
        print("3.Chauvegarder les commande:")
        print("4.Charger les commande depuis le fichier")
        print("5.Statistique sur les commande")
        print("6.Rechercher une commande par numero")
        print("8.Quitter le programme")
        
        choix = input("Choisissez une option :")
        if choix == "1":
            ajouter_commande()
        elif choix == "2":
            afficher_commande()
        elif choix == "3":
            sauvegarder_commande()
        elif choix == "4":
            charger_commande()
        elif choix == "5":
            statistique_commande()
        elif choix == "6":
            rechercher_commande()
        elif choix == "8":
            print("Au revoir !")
            break
        else:
            print("Option invalide.Veuillez choisir une option valide.")
        
    
        
def valider_nom(nom):
    # Vérifie si le champ est vide
    if not nom :
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
    
    
def afficher_commande():
    if not commandes:
        return False
    else:
        return True
    
def ajouter_commande():
    if not commandes:
        return False
    else:
        return True
    
def sauvegarder_commande():
    if not commandes:
        return False
    else:
        return True
    
        
def charger_commande():
    if not commandes:
        return False
    else:
        return True 
    
def calcul_moyenne_mesures(commandes): 
    if not commandes:
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
    
def statistique_commande():

    if not commandes:
        return False
    else:
        return True 
    
def rechercher_commande():
    if not commandes:
        return False
    else:
        return True 
    
saisir_commande()
afficher_commande()