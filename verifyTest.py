# ==== ==== ==== ====
#
#   verifyTest.py
#
#   Recherche des informations sur un fichier de test Ruby
#
#   Dernière modification : 23/11/2018
#
#	Anthony, Geoffroy, Jérôme, Pierrick, Tim, Valentine, 2018
#
# ==== ==== ==== ====

# Liste des commande qui ouvrent des actions
lOpen=["if", "while", "for", "do", "class", "def"]


# TO DO : exception, retirer les noms des tests avant leur analyse
def rechercheEnd(lignes, ligneOpen):
    """
    Inspiré de count_fonction de trouve_fonction
    Recherche le numéro de la ligne du end qui correspond au mot clé de open demandé
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param ligneOpen: Le numéro de la ligne pour laquelle on recherche le end associé
    :return: Le numéro de la ligne du end associé
    """
    # On suppose qu'un mot clé de open ne renvoie pas en end sur la même ligne si c'est le premier mot clé de open de sa ligne
    openCount = 1                               # openCount mesure le "niveau logique dans le code"
    for k in range(ligneOpen+1, len(lignes)):   # On itère sur chaque ligne dans la partie du fichier située après la ligne du départ
        #print(lignes[k])
        mots = lignes[k].strip().split()        # On sépare chaque ligne en plusieurs mots
        isIntoQuotes = False
        for mot in mots:
            if mot[0] == '"':                   # On ne souhaite pas analyser le contenu du nom des fichiers (il peux contenir des mots-clé ruby)
                isIntoQuotes = True
            if mot[-1] == '"':
                isIntoQuotes = False
            if isIntoQuotes == False:
                if mot == "end":                # Contrôle si la ligne contient des end
                    openCount -= 1
                for iOpen in lOpen:             # Contrôle si la ligne contient un mot clé de open
                    if mot == iOpen:
                        openCount += 1
                if openCount == 0:              # Ce cas advient lorsqu'on sort du "niveau logique dans le code" de départ
                    return k                    # On peux alors renvoyer le numéro de la ligne correspondante
    return -1                                   # On renvoie un code d'erreur si on ne trouve pas la ligne recherchée


# TO DO : exception
def isTest(lignes):
    """
    Vérifie que le fichier envoyé est bien un fichier de tests
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :return: True si le fichier est bien un fichier de tests Ruby, False sinon
    """
    for ligne in lignes:                                # On itère sur les lignes du tableau représentant le fichier
        if "require" in ligne:                          # La commande pour inclure doit être présente dans les fichiers de test
            mots = ligne.strip().split()                # On transforme chaque ligne en liste de mots
            for i in range(len(mots)):                  # On itère sur les mots
                if mots[i] == "require":                # On repère le mot correspondant à l'inclusion
                    for j in range(i+1, len(mots)):     # On itère sur les mots suivant l'instruction d'inclusion
                        if mots[j] == "'test_helper'":  # Le fichier test_helper doit être inclu au début des fichiers de test
                            return True
    return -1


# TO DO : exception
def countTests(lignes):
    """
    Compte le nombre de tests dans un fichier et les sépare
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :return: Un tuple constitué du nombre de tests dans le fichier et d'un dictionnaire avec le nom des tests pour indice et le tableau contenant les lignes associées pour valeur
    """
    if isTest(lignes):                                      # On vérifie tout d'abord que le fichier est un fichier de test valide
        nombreTests = 0
        dicTests = {}
        for numLigne in range(len(lignes)):                 # On itère sur les indices des lignes du fichier
            mots = lignes[numLigne].strip().split()         # On transforme chaque ligne du fichier en liste de mots
            if "test" in mots:                              # On cherche le début d'un test
                nomTest = ""
                for i in range(len(mots)):
                    if mots[i] == "test":                   # On répère précisément le début du test
                        nombreTests += 1                    # On incrément le compteur de tests
                        for j in range(i+1, len(mots)):     # On itère sur la liste des mots suivant le mot-clé test
                            nomTest += mots[j]              # Ces mots constitue le nom et la description du test
                            nomTest += " "
                            if mots[j][-1] == '"':          # Le nom et la description du test s'arrêtent après les quotes finales
                                break
                        nomTest = nomTest[1:-2]             # On retire les quotes inutiles dans le nom
                        dicTests[nomTest] = ""
                        break
                ligneEnd = rechercheEnd(lignes, numLigne)   # On récupère la ligne de fin associée au test
                #print(numLigne, ligneEnd)
                paragrapheTest = ""
                for j in range(numLigne, ligneEnd+1):       # On itère sur les lignes du test
                    paragrapheTest += lignes[j] + "\n"      # On enregistre les lignes du test
                dicTests[nomTest] = paragrapheTest          # On place cet enregistrement dans un dictionnaire
        return (nombreTests, dicTests)
    else:
        return isTest(lignes)                               # On retourne un code d'erreur si le fcichier n'est pas un fichier de test valide


def countAsserts(lignes, dicTests = False):
    """
    Compte le nombre de tests dans un fichier et les sépare
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param dicTests: une des valeurs de retour de la fonction countTests pour optimiser les calculs si elle a déjà été appelée avant
    :return: Un tuple constitué du nombre d'asserts dans le fichier et d'un dictionnaire avec le nom des tests pour indice et le tableau contenant les asserts associés pour valeurs
    """
    if not dicTests:                                                                # On retrouve les tests du fichier s'ils ne sont pas fournis
        dicTests = countTests(lignes)[1]
        print("recalcul")
    nombreAsserts = 0
    dicAsserts = {}
    for key in dicTests.keys():                                                     # On itère sur les tests retrouvés dans le fichier
        dicAsserts[key] = []
        lignesKey = []
        lignesKey.append("")
        actualLigneKey = 0
        for lettre in dicTests[key]:                                                # On recherche la ligne associée à la fin du test à partir du contenu enregistré de celui-ci
            if lettre == "\n":
                lignesKey.append("")
                actualLigneKey += 1
            else:
                lignesKey[actualLigneKey] += lettre
        for ligne in lignesKey:                                                     # On itère sur les lignes de démarrage des tests
            mots = ligne.strip().split()
            if "assert" in mots or "assert_not" in mots or "assert_equal" in mots:  # On recherche les mots-clés des assertions dans les tests
                nombreAsserts += 1
                dicAsserts[key].append(ligne)
    return (nombreAsserts, dicAsserts)


def printStatsTests (lignes, voirContenu = True):
    """
    Affiche les informations statistiques à propos des tests
    :param lignes: Un tableau contenant des strings correspondantes aux différentes lignes du texte
    :param voirContenu: La fonction permet à l'utilisateur d'afficher le contenu des tests si la valeur est True, et passe cette partie sinon
    :return: None
    """
    resultTest = countTests(lignes)                                                                                         # On effectue une seule fois la recherche des tests
    resultAssert = countAsserts(lignes, resultTest[1])                                                                      # On effectue une seule fois la recherche des asserts
    print("")                                                                                                               # On affiche le nombre de tests
    print("Nombre de tests dans le fichier : " + str(resultTest[0]))
    listeStrNumsTests = []
    for i in range(resultTest[0]):
        listeStrNumsTests.append(str(i+1))
    print("")                                                                                                               # On affiche le nombre d'asserts
    print("Nombre d'asserts dans le fichier : " + str(resultAssert[0]))
    print("")                                                                                                               # On affiche le nom des tests
    print("Les noms des test sont : ")
    for i in range(len(resultTest[1].keys())) :                                                                             # On itère sur les tests repérés
        nomTest = list(resultTest[1].keys())[i]
        print ("    " + str(i+1) + ') "' + nomTest + '" qui contient ' + str(len(resultAssert[1][nomTest])) + " assert(s)") # On affiche le nombre d'asserts par test
    askingResults = True
    askedResult = 0
    while askingResults and voirContenu:                                                                                    # On permet à l'utilisateur de voir le contenu d'un test
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
    while askingResults and voirContenu:                                                                                    # On permet à l'utilisateur de voir les asserts contenus dans un test
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
