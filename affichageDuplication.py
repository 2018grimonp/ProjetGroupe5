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

codeControle=readLines("testControle.rb")
precision=80

def creation_string(code):
    donnees=duplicationFonction.retuour_resresultats_similitude(code,precision,codeControle)
    copies_percent=donnees[0]/donnees[1]*100
    graph="Fonctions copiées-Donne le nombre de fonctions suceptibles d'avoir été copiées (avec une précision minimale de "+str(precision)+"%)  pourcentage de duplication :"+str(donnees[2])+ "%-fonction originale+fonctions copiées-"+str(100-copies_percent)+"-Multiplicateur de note: "+str(1-copies_percent/100)+"-|"
    return (graph,1-copies_percent/100)

def creation_string_duplication_interne(Code):
    liste_fonction=duplicationInterne.fonction_double(Code,precision)
    l_double=0
    for k in liste_fonction:
        l_double+=k["longueur"]*k["copie"]
    graph="Ligne de code inutile-Donne le pourcentage de lignes de code qui sont en double.-Lignes doublées+Lignes utiles -"+str(l_double/len(Code)*100)+"-Malus: -"+str(5*l_double/len(Code))+"-|"
    return(graph,-5*l_double/len(Code))
