from commentaires import retirerCom
from commentaires import printCom 

from checkIndentation import retirerIndentation
from checkIndentation import printIndentation

from test_variables import print_test_variable

from trouve_fonction import printFonction

from verifyTest import printStatsTests

def readLines(l):  # retire les '/n' d'un fichier texte 
    L=[]
    fp=open(l,'r')
    lines=fp.readlines()
    for line in lines:
        line=line.replace('\n', '')
        L.append(line)
    return L

print ('Nom du fichier à analyser :')

#On rentre le fichier que l'on veut manipuler
path=input()
lines=readLines(path)

#Affichage d'informations sur les commentaires puis suppression des commentaires.
print("----- COMMENTAIRES -----")
printCom(lines)
lines=retirerCom(lines)

#Extraction et retrait des indentations et affichage d'informations sur la correction des indentations.
print("----- INDENTATIONS -----")
printIndentation(lines)
lines=retirerIndentation(lines)

#Parsing des fonctions présentes dans le code et affichage de leur nombre de lignes.
print("----- FONCTIONS  -----")
printFonction(lines)

#Parsing des tests présents dans le code et affichage de données à leur sujet.
print("----- VERIFICATION DES TESTS  -----")
printStatsTests(lines)

#Parsing des variables présentes dans le code et affichage d'informations à leur sujet.
print("----- VARIABLES  -----")
print_test_variable(lines)



