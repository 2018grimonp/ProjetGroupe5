from commentaires import retirerCom
from commentaires import printCom 

from checkIndentation import retirerIndentation
from checkIndentation import printIndentation

from trouve_fonction import printFonctions

from verifyTest import printStatsTests

def readLines(l):  # retire les '/n' d'un fichier texte 
    L=[]
    with open(l,'r') as fp:
        for line in fp:
            line=line.replace('\n', '')
            L.append(line)
    print(L)
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

#Parsing des fonctions présentes dans le code et affichages de leur nombre de lignes
print("----- FONCTIONS  -----")
printFonctions(lines)

print("----- VERIFICATION DES TESTS  -----")
printStatsTests(lines)


