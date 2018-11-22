from commentaires import retirerCom
from commentaires import printCom 

from checkIndentation import retirerIndentation
from checkIndentation import printIndentation

from test_variables import countVariables

from check_case import printNommageCoherent

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

#String qui représente le contenu du fichier results.txt qui sera fournis à l'interface graphique
results_txt=""

#Affichage d'informations sur les commentaires puis suppression des commentaires.
print("----- COMMENTAIRES -----")
#results_txt=results_txt+printCom(lines)
lines=retirerCom(lines)

#Extraction et retrait des indentations et affichage d'informations sur la correction des indentations.
print("----- INDENTATIONS -----")
results_txt=results_txt+printIndentation(lines)
lines=retirerIndentation(lines)

#Parsing des fonctions présentes dans le code et affichage de leur nombre de lignes.
print("----- FONCTIONS  -----")
printFonction(lines)

#Parsing des tests présents dans le code et affichage de données à leur sujet.
print("----- VERIFICATION DES TESTS  -----")
printStatsTests(lines)

#Parsing des variables présentes dans le code et affichage d'informations à leur sujet.
print("----- VARIABLES  -----")
variables_list=countVariables(lines)
printNommageCoherent(variables_list)


results=open("results.txt","w")
results.write(results_txt)
results.close()



