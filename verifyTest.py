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
lOpen=["if", "while", "for", "do", "class", "def"]


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
        #print(lignes[k])
        mots = lignes[k].strip().split()
        isIntoQuotes = False
        for mot in mots:
            if mot[0] == '"':
                isIntoQuotes = True
            if mot[-1] == '"':
                isIntoQuotes = False
            if isIntoQuotes == False:
                if mot == "end":    # Contrôle si la ligne contient des end
                    openCount -= 1
                for iOpen in lOpen: # Contrôle si la ligne contient un mot clé de open
                    if mot == iOpen:
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
            mots = lignes[numLigne].strip().split()
            if "test" in mots:
                nomTest = ""
                for i in range(len(mots)):
                    if mots[i] == "test":
                        nombreTests += 1
                        for j in range(i+1, len(mots)):
                            nomTest += mots[j]
                            nomTest += " "
                            if mots[j][-1] == '"':
                                break
                        nomTest = nomTest[1:-2]
                        dicTests[nomTest] = ""
                        break
                ligneEnd = rechercheEnd(lignes, numLigne)
                print(numLigne, ligneEnd)
                paragrapheTest = ""
                for j in range(numLigne, ligneEnd+1):
                    paragrapheTest += lignes[j] + "\n"
                dicTests[nomTest] = paragrapheTest
        return (nombreTests, dicTests)
    else:
        return -1


def countAsserts(lignes, dicTests = False):
    """
    Compte le nombre de tests dans un fichier et les sépare
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param dicTests: une des valeurs de retour de la fonction countTests pour optimiser les calculs si elle a déjà été appelée avant
    :return: Un tuple constitué du nombre d'asserts dans le fichier et d'un dictionnaire avec le nom des tests pour indice et le tableau contenant les asserts associés pour valeurs
    """
    if not dicTests:
        dicTests = countTests(lignes)
        print("recalcul")
    nombreAsserts = 0
    dicAsserts = {}
    for key in dicTests.keys():
        dicAsserts[key] = []
        for ligne in dicTests[key]:
            mots = ligne.strip().split()
            if "assert" in mots:
                nombreAsserts += 1
                dicAsserts[key].append(ligne)
    return dicAsserts


# TO DO : compter le nombre d'assert, rectfier le bug contenu des tests
def printStatsTests (lignes, voirContenu = True):
    """
    Affiche les informations statistiques à propos des tests
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param voirContenu: La fonction permet à l'utilisateur d'afficher le contenu des tests si la valeur est True, et passe cette partie sinon
    :return: None
    """
    result_0 = countTests(lignes)
    result_1 = countAsserts(lignes, result_0[1])
    print("")
    print("Nombre de tests dans le fichier : " + str(result_0[0]))
    listeStrNumsTests = []
    for i in range(result_0[0]):
        listeStrNumsTests.append(str(i+1))
    print("")
    print("Les noms de ces test sont : ")
    for i in range(len(result_0[1].keys())) :
        nomTest = list(result_0[1].keys())[i]
        print ("    " + str(i+1) + ") " + nomTest + " qui contient " + result_1)
    # A débugger
    askingResults = True
    askedResult = 0
    while askingResults and voirContenu:
        print("")
        askedResult = input("Pour voir le contenu d'un test entrer son numéro, sinon entrer quoique ce soit d'autre : ")
        if askedResult in listeStrNumsTests:
            key = list(result_0[1].keys())[int(askedResult)-1]
            print("")
            print('Le contenu du test ' + askedResult + ' est :')
            print("")
            print(result_0[1][key])
        else:
            askingResults = False
