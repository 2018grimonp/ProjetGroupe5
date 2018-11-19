# ==== ==== ==== ====
#
#   verifyTest.py
#
#   Recherche des informations sur un fichier de test Ruby
#
#   Dernière modification : 19/11/2018
#
#	2018
#
# ==== ==== ==== ====

# Liste des commande qui ouvrent des actions
l_open=["if","while","for","do","class"]

#degrossir + exception
def rechercheEnd(lignes, ligneOpen):
    """
    Inspiré de count_fonction de trouve_fonction
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param ligneOpen: Le numéro de la ligne pour laquelle on recherche le end associé
    :return: Le numéro de la ligne du end associé
    """
    # On suppose qu'un mot clé de open ne renvoie pas en end sur la même ligne si c'est le premier mot clé de open de sa ligne
    open_count=0
    fonction_open=False
    def_open=-1
    for k in range(len(lignes)):
        if "end" in ligne
        if Code[:3]=="def" :
            if fonction_open :                  #test si une fonction est déjà ouverte
                return("Erreur fonction lingne "+str(k))
            else :
                fonction_open=True
            ListeLongeurFonction.append(k)      #sauvegarde l'indice de début de la fonction
            def_open=open_count
            open_count+=1
        if ligne_open(k) :      #controle si la ligne ouvre des commandes
            open_count+=1
        if Code[:3]=="end" :    #controle si la ligne ferme des commandes
            open_count-=1
            if open_count== def_open :
                ListeLongeurFonction[-1]=k-ListeLongeurFonction[-1]-1   #calcul la longueur de la fonction (def et end exclus)
    return(ListeLongeurFonction)


def isTest(lignes):
    """
    Vérifie que le fichier envoyé est bien un fichier de tests
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :return: True si le fichier est bien un fichier de tests Ruby, False sinon
    """
    
    for ligne in lignes:
        if "require" in ligne:
            mots = ligne.strip().split()
            for i on range(len(mots)):
                if mots[i] == "require":
                    for j in range(i+1, len(mots)):
                        if mots[j] == "'test_helper'":
                            return True
    return False

#v0.1
# Ajouter isTest + exception
def countTests(lignes):
    """
    Compte le nombre de tests dans un fichier et les séparent
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :return: Un tuple constitué du nombre de tests dans le fichier et d'un dictionnaire avec le nom des tests pour indice et le tableau contenant les lignes associées pour valeur
    """
    
    nombreTests = 0
    for ligne in lignes:
        if "test" in ligne:
            mots = ligne.strip().split()
                for i on range(len(mots)):
                    if mots[i] == "test":
                        nombreTests += 1
    return nombreTests
