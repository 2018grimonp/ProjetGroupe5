import duplicationFonction
import duplicationInterne

def readLines(l):  # retire les '/n' d'un fichier texte
    L=[]
    fp=open(l,'r')
    lines=fp.readlines()
    for line in lines:
        line=line.replace('\n', '')
        L.append(line)
    return L

code=readLines("test.rb")
codeControle=readLines("testControle.rb")
precision=80

def creation_string(code,codeControle,precision):
    donnees=duplicationFonction.retuour_resresultats_similitude(code,precision,codeControle)
    copies_percent=donnees[0]/donnees[1]
    graph="Fonction copié-donne le nombre de fonctions suceptible d'e^tre fraudé (avec une précision minimale de "+str(precision)+"% -fonction originale+fonctions copiées-"+str(copies_percent)+"-Multiplicateur de note: "+str(copies_percent/10)+"/10 pourcentage de duplication :"+str(donnees[2])+"-|"
    return (graph)

