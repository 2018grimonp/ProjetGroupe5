from commentaires import retirerCom
from commentaires import printCom 

from checkIndentation import retirerIndentation
from checkIndentation import printIndentation

from trouve_variables import countVariables

from check_case import returnmain 

from trouve_fonction import printFonction
from affichageDuplication import creation_string

from verifyTest import printStatsTests

from appelvariable import graphiquenote

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
txt,points_c,a=printCom(lines)
results_txt=results_txt+str(txt)
lines=retirerCom(lines)

#Extraction et retrait des indentations et affichage d'informations sur la correction des indentations.
print("----- INDENTATIONS -----")
txt,points_i=printIndentation(lines)
results_txt=results_txt+txt
lines=retirerIndentation(lines)

#Parsing des fonctions présentes dans le code et affichage de leur nombre de lignes.
print("----- FONCTIONS  -----")
txt,points_f1=printFonction(lines)
results_txt=results_txt+txt
txt,points_f2=creation_string(lines)
results_txt=results_txt+txt

#Parsing des tests présents dans le code et affichage de données à leur sujet.
print("----- VERIFICATION DES TESTS  -----")
txt,points_t=printStatsTests(lines,False)
results_txt=results_txt+txt

#Parsing des variables présentes dans le code et affichage d'informations à leur sujet.
print("----- VARIABLES  -----")
variables_list=countVariables(lines)
txt,points_v=returnmain(variables_list)
results_txt=results_txt+txt
txt,points_v2=graphiquenote(lines)
results_txt=results_txt+txt

points_i=round(points_i*points_f2)
points_c=round(points_c*points_f2)
points_t=round(points_t*points_f2)
points_v=round(points_v*points_f2)
points_v2=round(points_v2*points_f2)
note=round((points_i+points_c+points_t+points_v+points_v2)/5)
results_txt=results_txt+"Synthèse--Indentation+Commentaires+Tests+Nommage+Variables utilisées+Points perdus-"+str(points_i*100//50)+"+"+str(points_c*100//50)+"+"+str(points_t*100//50)+"+"+str(points_v*100//50)+"+"+str(points_v2*100//50)+"-Note : "+str(note)+"/10-|"
results=open("results.txt","w")
results.write(results_txt)
results.close()

print(note)

