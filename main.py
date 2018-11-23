def readLines(l):  # retire les '\n' d'un fichier texte 
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

#String qui représente le contenu du fichier results.txt qui sera fournis à l'interface graphique
results_txt=""

#Affichage d'informations sur les commentaires puis suppression des commentaires.
print("----- COMMENTAIRES -----")
results_txt=results_txt+printCom(lines)[0]
lines=retirerCom(lines)

#Extraction et retrait des indentations et affichage d'informations sur la correction des indentations.
print("----- INDENTATIONS -----")
results_txt=results_txt+printIndentation(lines)
lines=retirerIndentation(lines)

#Parsing des fonctions présentes dans le code et affichage de leur nombre de lignes.
print("----- FONCTIONS  -----")
results_txt=results_txt+printFonction(lines)[0]

t=input()           #on rentre le fichier que l'on veut manipuler

T=readLines(t)

def nbassert(lines):
    """Compte le nombre de tests et d'asserts dans le fichier test"""
    t=0                 #nombre de tests
    a=0                 #nombre d'asserts
    for i in lines :            #on regarde dans chaque élément de la liste combien il y a de test et d'assert 
        if 'test' in i :        #il ne peut pas y avoir 'test' et 'assert' dans la meme ligne
            t=t+1
        elif 'assert' in i:
            a=a+1
    return (t,a)




