# ==== ==== ==== ====
#
#   test_variable.py
#
#   Recherche des informations sur les variables dans un fichier Ruby
#
#   Dernière modification : 21/11/2018
#
#	2018
#
# ==== ==== ==== ====

# Ancienne version légèrement modifiée



# v0.1

def countVariables(lines, redondance = False):
    """
    Analyse le tableau des lignes envoyé et renvoie la liste des variables déclarées touvées
    :param lines: une liste de lignes (sans les '/n')
    :param redondance": le tableau renvoyé sera avec redondance pour True, et sans redondance pour False
    :return: un tableau contenant les noms des variables
    """
    nbVariables = 0
    tabVariables = []   # Stock les variables
    for line in lines:
        print(line)
        tabline=line.split(" ")
        print(tabline)
        for mot in line.split(" "):   #car quand un égale est collé, on a mots = [\"maVariable= \", \"jhu\",..."]
            if mot.find("=")!=-1:
                if mot.find("==")==-1:
                    mot=mot.strip("=")
                    print(mot)
                    if len(mot)!=0:   #ce n'est pas juste un espace
                        nbVariables+=1
                        tabVariables.append(mot)
        if "=" in line:
            if "==" not in line:
                mots = line.strip().split()
                indiceEqual = -1
                for i in range(len(mots)):
                    if mots[i] == "=":
                        indiceEqual = i
                        nbVariables += 1
                        tabVariables.append(mots[indiceEqual - 1])
                        break
    #tabVariablesSansDoublons = set(tabVariables)
    #print(tableau_variables_sans_doublons)
    #nbVariables = len(tableau_variables_sans_doublons)
    #str_variables_utiles=",".join(tableau_variables_sans_doublons)
    #print ("Il y a "+str(nombre_variables)+ ". Elles s'appellent " + str_variables_utiles +" .")
    #print(tableau_variables_sans_doublons)
    return tabVariables
#print(countVariables(["bh vugg= grte gtr", "byug retdt = gtre", "cb beaz == hjbu nji", "frez rezf== fe fre"]))


def snailVariables(lines, listeVariables):
    """
    Supprime du tableau de ligne envoyé les variables de la liste et renvoie le tableau
    :param lines: une liste de lignes (sans les '/n')
    :param listeVariables: la liste des variables à supprimer
    :return: le tableau originel privé des varaiables à retirer
    """
    for ligneIndex in range(len(lines)):
        mots = lines[ligneIndex].strip().split()
        for i in range(len(mots)-1, -1, -1):
            if (mots[i] in listeVariables) or (mots[i][-1] == "," and mots[i][:-1] in listeVariables):
                mots.pop(i)
        lines[ligneIndex] = " ".join(mots)
    return lines
