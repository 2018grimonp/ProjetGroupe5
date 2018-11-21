# ==== ==== ==== ====
#
#   verifyTest.py
#
#   Recherche des informations sur un fichier de test Ruby
#
#   Dernière modification : 21/11/2018
#
#	2018
#
# ==== ==== ==== ====

# Liste des commande qui ouvrent des actions
lOpen=["if", "while", "for", "do", "class"]


# TO DO : exception, virer les noms des tests avant leur analyse
def rechercheEnd(lignes, ligneOpen):
    """
    Inspiré de count_fonction de trouve_fonction
    Recherche le numéro de la ligne du end qui correspond au mot clé de open demandé
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param ligneOpen: Le numéro de la ligne pour laquelle on recherche le end associé
    :return: Le numéro de la ligne du end associé
    """
    # On suppose qu'un mot clé de open ne renvoie pas en end sur la même ligne si c'est le premier mot clé de open de sa ligne
    openCount = 1
    for k in range(ligneOpen+1, len(lignes)):
        mots = lignes[k].strip().split()
        if "end" in mots:   # Contrôle si la ligne contient des end
            openCount -= 1
        for iOpen in lOpen: # Contrôle si la ligne contient un mot clé de open
            if iOpen in mots:
                openCount += 1
        if openCount == 0:
            return k
    return -1


def isTest(lignes):
    """
    Vérifie que le fichier envoyé est bien un fichier de tests
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :return: True si le fichier est bien un fichier de tests Ruby, False sinon
    """
    
    for ligne in lignes:
        if "require" in ligne:
            mots = ligne.strip().split()
            for i in range(len(mots)):
                if mots[i] == "require":
                    for j in range(i+1, len(mots)):
                        if mots[j] == "'test_helper'":
                            return True
    return -1


# TO DO : exception, refactoriser
def countTests(lignes):
    """
    Compte le nombre de tests dans un fichier et les sépare
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :return: Un tuple constitué du nombre de tests dans le fichier et d'un dictionnaire avec le nom des tests pour indice et le tableau contenant les lignes associées pour valeur
    """

    if isTest(lignes):
        nombreTests = 0
        dicTests = {}
        for numLigne in range(len(lignes)):
            nombreTestsDansLigne = 0
            if "test" in lignes[numLigne]:
                mots = lignes[numLigne].strip().split()
                for i in range(len(mots)):
                    if mots[i] == "test":
                        nombreTestsDansLigne += 1
                        if nombreTestsDansLigne == 1:
                            nombreTests += 1
                            nomTest = ""
                            for j in range(i+1, len(mots)):
                                nomTest += mots[j]
                                nomTest += " "
                                if mots[j][-1] == '"':
                                    break
                            nomTest = nomTest[1:-2]
                            dicTests[nomTest] = ""
                if nombreTestsDansLigne == 1:
                    ligneEnd = rechercheEnd(lignes, numLigne)
                    print(numLigne, ligneEnd)
                    paragrapheTest = ""
                    for j in range(numLigne, ligneEnd+1):
                        paragrapheTest += lignes[j] + "\n"
                    dicTests[nomTest] = paragrapheTest
        return (nombreTests, dicTests)
    else:
        return -1


# TO DO : compter le nombre d'assert, rectfier le bug contenu des tests
def printStatsTests (lignes):
    """
    Affiche les informations statistiques à propos des tests
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :return: None
    """
    result = countTests(lignes)
    print("")
    print("Nombre de tests dans le fichier : " + str(result[0]))
    listeStrNumsTests = []
    for i in range(result[0]):
        listeStrNumsTests.append(str(i+1))
    print("")
    print("Les noms de ces test sont : ")
    for i in range(len(result[1].keys())) :
        print ("    " + str(i+1) + ") " + list(result[1].keys())[i])
    # A débugger
    askingResults = True
    askedResult = 0
    while askingResults:
        print("")
        askedResult = input("Pour voir le contenu d'un test entrer son numéro, sinon entrer quoique ce soit d'autre : ")
        if askedResult in listeStrNumsTests:
            key = list(result[1].keys())[int(askedResult)-1]
            print("")
            print('Le contenu du test ' + askedResult + ' est :')
            print("")
            print(result[1][key])
        else:
            askingResults = False
