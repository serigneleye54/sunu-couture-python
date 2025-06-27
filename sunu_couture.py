client = {
    "nom": input("Entrez le nom : "),
    "prenom": input("Entrez le prénom : "),
    "telephone": input("Entrez le numéro de téléphone : "),
    "email": input("Entrez l'adresse email : "),
    "type_de_vetements": input("Entrez le type de vêtements (ex: robe, costume, chemise, jean, etc.) : "),
    "sexe" : input("Sexe (H/F) : "),
    "mesures": {
        "taille": input("Entrez la taille (en cm) : "),
        "hanche": input("Entrez le tour de hanche (en cm) : "),
        "longueur": input("Entrez la longueur (en cm) : "),
    },
    "options": {
        "livraison": input("Livraison ? (oui/non) : "),
        "retouche": input("Retouche ? (oui/non) : "),
        "commentaire": input("Commentaire : "),
    }
}