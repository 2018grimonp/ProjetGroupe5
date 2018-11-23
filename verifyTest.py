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


# TO DO : eception
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


# TO DO : exception
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
        return isTest(lignes)


def countAsserts(lignes, dicTests = False):
    """
    Compte le nombre de tests dans un fichier et les sépare
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param dicTests: une des valeurs de retour de la fonction countTests pour optimiser les calculs si elle a déjà été appelée avant
    :return: Un tuple constitué du nombre d'asserts dans le fichier et d'un dictionnaire avec le nom des tests pour indice et le tableau contenant les asserts associés pour valeurs
    """
    if not dicTests:
        dicTests = countTests(lignes)[1]
        print("recalcul")
    nombreAsserts = 0
    dicAsserts = {}
    for key in dicTests.keys():
        dicAsserts[key] = []
        lignesKey = []
        lignesKey.append("")
        actualLigneKey = 0
        for lettre in dicTests[key]:
            if lettre == "\n":
                lignesKey.append("")
                actualLigneKey += 1
            else:
                lignesKey[actualLigneKey] += lettre
        for ligne in lignesKey:
            mots = ligne.strip().split()
            if "assert" in mots or "assert_not" in mots or "assert_equal" in mots:
                nombreAsserts += 1
                dicAsserts[key].append(ligne)
    return (nombreAsserts, dicAsserts)


# TO DO : compter le nombre d'assert, rectfier le bug contenu des tests
def printStatsTests (lignes, voirContenu = True):
    """
    Affiche les informations statistiques à propos des tests
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param voirContenu: La fonction permet à l'utilisateur d'afficher le contenu des tests si la valeur est True, et passe cette partie sinon
    :return: None
    """
    resultTest = countTests(lignes)
    resultAssert = countAsserts(lignes, resultTest[1])
    print("")
    print("Nombre de tests dans le fichier : " + str(resultTest[0]))
    listeStrNumsTests = []
    for i in range(resultTest[0]):
        listeStrNumsTests.append(str(i+1))
    print("")
    print("Nombre d'asserts dans le fichier : " + str(resultAssert[0]))
    print("")
    print("Les noms des test sont : ")
    nombre1Assert = 0
    for i in range(len(resultTest[1].keys())) :
        nomTest = list(resultTest[1].keys())[i]
        print ("    " + str(i+1) + ') "' + nomTest + '" qui contient ' + str(len(resultAssert[1][nomTest])) + " assert(s)")
        if len(resultAssert[1][nomTest]) == 1:
            nombre1Assert += 1
    askingResults = True
    askedResult = 0
    while askingResults and voirContenu:
        print("")
        askedResult = input("Pour voir LE CONTENU d'un test entrer son numéro, sinon entrer quoique ce soit d'autre : ")
        if askedResult in listeStrNumsTests:
            key = list(resultTest[1].keys())[int(askedResult)-1]
            print("")
            print('Le contenu du test ' + askedResult + ' est :')
            print("")
            print(resultTest[1][key])
        else:
            askingResults = False
    askingResults = True
    askedResult = 0
    while askingResults and voirContenu:
        print("")
        askedResult = input("Pour voir LES ASSERTS d'un test entrer son numéro, sinon entrer quoique ce soit d'autre : ")
        if askedResult in listeStrNumsTests:
            key = list(resultTest[1].keys())[int(askedResult)-1]
            print("")
            print('Les asserts du test ' + askedResult + ' sont :')
            print("")
            print(resultAssert[1][key])
        else:
            askingResults = False
    note1 = int((1-nombre1Assert/resultTest[0])*50)/10
    note2 = points(resultTest[0],resultAssert[0]/resultTest[0])
    graphique = 'Tests-'+str(note2[1])+'-Qualité des tests+Tests utiles+Points perdus-'+str(note2[0]*10)+'+'+str(note1*10)+'-Note : '+str(note1+note2[0])+'/10-|'
    return graphique, note1+note2[0]

def points(tests, asserts):
    '''
    Donne le nombre de points obtenus quant à l'écriture des tests
    :param fonctions: la liste des tests du code
    :param asserts: le nombre d'asserts
    :return: la note sur 10 ainsi qu'un commentaire associé
    '''
    L = tests
    if L == 0:
        return 0, 'Ce candidat n\'utilise pas de tests'
    else:
        if asserts < 2:
            note = 1
            commentaire = 'Il n\' y a pas assez d\'asserts'
        elif asserts < 5:
            if L < 5:
                note = 2
                commentaire = 'Il y a pas assez d\'asserts si de tests'
            elif L < 20:
                note = 5
                commentaire = 'Les tests sont très satisfaisants'
            else:
                note = 1
                commentaire = 'Il y a trop de tests'
        elif asserts < 15:
            if L < 2:
                note = 2
                commentaire = 'Il y a pas assez de tests mais assez d\'asserts'
            elif L < 5:
                note = 4
                commentaire = 'Les tests sont de taille raisonnable, il y a assez d\'asserts'
            elif L < 20:
                note = 5
                commentaire = 'Le tests sont bien gérés'
            else:
                note = 2
                commentaire = 'Il y a trop de tests'
        else:
            if L < 5:
                note = 1
                commentaire = 'Il y a trop d\'asserts, et trop de tests'
            elif L < 20:
                note = 2
                commentaire = 'Trop d\'asserts, niveau nombre de tests ça va'
            else:
                note = 1
                commentaire = 'Trop d\'asserts, trop de tests'
    return note, commentaire

def fichierLecture():
    """
    Ouvre le fichier event_candidate_a.rb.rb, juste pour pouvoir tester les fonctions (à virer)
    :return: la liste des lignes du fichier
    """
    try:
        fichier = open("./test.rb", "rt")
        ligneListe = fichier.readlines()
        return ligneListe
    except IOError:
        print("Erreur fichier")

