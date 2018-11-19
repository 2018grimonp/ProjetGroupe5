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
