import re
#definition du dictionnaire :

def  saisir_commande() :
    
    client = {}
    print("Entrez vos identifiants")
    while True:
        nom= input("Entrez le nom : ")
        if valider_nom(nom) == False :
            print("ce champ est requis.")
        elif nom.isdigit():
            print("les lettres sont seulements autorisées")
        else: 
            #ajouter un element dans un dictionnaire
            client["nom"] = nom
            break
        
    
    while True:
        prenom= input("Entrez le prenom: ")
        if valider_prenom(prenom) == False :
            print("ce champ est requis.")
        elif prenom.isdigit():
            print("les lettres sont seulements autorisées")
        else:
            client["prenom"] = prenom
            break
        
    
    while True:
        telephone= input("entrer le numéro de téléphone:")
        if valider_numero(telephone) == False :
            print("ce champ est requis.")
        elif telephone.isalpha():
             print("les chiffres sont seulements autorisées")
        else:
            client ["téléphone"] = telephone
            break 
        
    
    while True:
        email= input("entrer l'adresse email:")
        if not email:
            print("ce champ est requis.")
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
            print("ce champ est requis.")
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
            print("ce champ est requis.")
        elif sexe in liste_sexe :
            #concaténation avec f
            print(f"vous etes un(e):{sexe}")
            break
        else:
            print("Invalide.Veuillez saisir h(homme) ou f(femme):")
            
    print("\nVos mesures :")
    while True:
        try:
            mesure = float(input("Veuillez saisir la taille:"))
            if mesure != 0:
                break
            else:
                print("Taille doit etre strictement superieur a zero.")
        except ValueError:
            print("Taille doit etre un nombre.")
            
    while True:
        try:
            mesure = float(input("Veuillez saisir hanche:"))
            if mesure != 0:
                break
            else:
                print("Hanche doit etre strictement superieur a zero.")
        except ValueError:
            print("Hanche doit etre un nombre.")
             
    while True:        
        try:
            mesure = float(input("Veuillez saisir la longueur:"))
            if mesure != 0:
                break
            else:
                print("Longueur doit etre strictement superieur a zero.")
        except ValueError:
            print("Longueur doit etre un nombre.")
            
    print("\nVos options")        
    choix = ["oui","non"]
    while True:
        livraison = input("Entrez oui ou non pour livraison:").lower()  
        if livraison in choix:
            print(f"Vous avez choisi :{livraison}")
            break
        else:
            print("choix non valide")
            
    choix = ["oui","non"]
    while True:
        retouche = input("Entrez oui ou non pour retouche:").lower()  
        if retouche in choix:
            print(f"Vous avez choisi :{retouche}")
            break
        else:
            print("choix non valide")
            
    
             
    client = {
        "options": {
           
            "commentaire": input("Veuillez laisser un commentaire : "),
        }
    }
        
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
    
        
    
    
saisir_commande()
        