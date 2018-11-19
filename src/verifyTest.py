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
lOpen=["if","while","for","do","class"]

# TO DO : exception
def rechercheEnd(lignes, ligneOpen):
    """
    Inspiré de count_fonction de trouve_fonction
    Recherche le numéro de la ligne du end qui correspond au mot clé de open demandé
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param ligneOpen: Le numéro de la ligne pour laquelle on recherche le end associé
    :return: Le numéro de la ligne du end associé
    """
    # On suppose qu'un mot clé de open ne renvoie pas en end sur la même ligne si c'est le premier mot clé de open de sa ligne
    open_count = 1
    for k in range(ligneOpen+1, len(lignes)):
        if "end" in ligne:  # Contrôle si la ligne contient des end
            open_count -= 1
        for iOpen in lOpen: # Contrôle si la ligne contient un mot lé de open
            if iOpen in ligne:
                open_count += 1
        if open_count == 0:
            return k
    return False


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

# v0.1
# TO DO : Ajouter isTest + exception
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
