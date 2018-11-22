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

"""
import re


def test_variables(lines, redondance = False):
    Analyse le tableau des lignes envoyé et renvoie la liste des variables déclarées touvées
    :param lines: une liste de lignes (sans les '/n')
    :param redondance": le tableau renvoyé sera avec redondance pour True, et sans redondance pour False
    :return: un tableau contenant les noms des variables
    nombre_variables=0
    tableau_variables=[]   #pour stocker les variables
    for line in lines:
        if line.find("=")>0:
            #print(line)
            tableau_avant_apres=line.split("=")    #on separe la chaine avant et apres le egale
            #print(tableau_avant_apres)
            string_avant=tableau_avant_apres[0]
            #print(string_avant)
            tableau_avant=string_avant.split(" ") #on recuper le nom de la variable, qui se trouve dans la derniere case du tableau
            print(tableau_avant[-1])
            if re.match("^[A-Za-z]$",tableau_avant[-1])!=None:  #s'il y a pas un espace avant le =
                tableau_variables.append(tableau_avant[-1])
            else:                                             #s'il y a un espace avant le =
                tableau_avant.pop()
                tableau_variables.append(tableau_avant[-1])
    tableau_variables_sans_doublons=set(tableau_variables)
    #print(tableau_variables_sans_doublons)
    nombre_variables=len(tableau_variables_sans_doublons)
    #str_variables_utiles=",".join(tableau_variables_sans_doublons)
    #print ("Il y a "+str(nombre_variables)+ ". Elles s'appellent " + str_variables_utiles +" .")
    print(tableau_variables_sans_doublons)
    return None
"""

# Nouvelle version


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