from trouve_fonction import count_fonction
from trouve_variables import countVariables

def numlignevarglo(lignes):             #lignes=fichier texte contenant toutes les lignes du code
    #va récupérer les indices des lignes en dehors des fonctions
    L=count_fonction(lignes)
    var=[]
    numligne= [i for i in range(1,len(lignes))]
    toRemove = []
    for i in range(len(L)):
        (deb,fin)=(L[i]['start'],L[i]['end'])    #on récupère la ligne de début et de fin de chaque fonction
        for k in range (deb, fin+1):
            #print(k)
            toRemove.append(k)                 #on retire les indices des lignes où il y a une fonction
    numLigneOk = []
    for i in numligne:
        if not i in toRemove:
            numLigneOk.append(i)
    return numLigneOk

def varglobal(lignes):
    #renvoie les variables globales et les indices des lignes où elles apparaissent
    L=numlignevarglo(lignes)
    vars=[]
    for i in L:
        #print("lol" +str(lignes[i-1]))
        var= countVariables([lignes[i-1]])                                  #appel fonction pour récupérer la variable dans la ligne i de lignes
        #print(var)
        if var:
            vars.append([var[0],i])                                         #var= un tableau avec comme seul élément une variable
    return vars
        
def varglobefore(i,lignes):
#prend en argument les lignes et i un indice et renvoie la liste des variables globales qui aparaissent avant cet indice
    L=varglobal(lignes)
    T=[]
    for k in L:
        if k[1]<i:
            T.append(k[0])
    return T

def textefonctions(lignes):             
    #renvoie une liste dont les éléments sont l'indice de début de la fonction et son texte
    listedico = count_fonction(lignes)
    textefonctions = []
    for i in range(len(listedico)):
        deb,fin = listedico[i]['start'],listedico[i]['end']
        fonction=lignes[deb:fin+1]
        textefonctions.append([deb,fonction])
    return textefonctions


def appelvar (lignes):                          #lignes=fichier texte contenant toutes les lignes du code
    #regarde si une variable a été utilisée 
    compteur=0                                  #compteur correspond au nombre de fois où une variable n'a pas été appelée    
    L=textefonctions(lignes)
    for i in range(len(L)) :    
        vars= countVariables(L[i][1])                    #vars = les variables dans la ième fonction 
        vars= vars + varglobefore(L[i][0], lignes)                #on rajoute les variables globales créées avant la fonction 
        for var in vars:
            if vars.count(var) ==1:
                compteur+=1
    return compteur

def graphiquenote(lignes):
    compteur = appelvar(lignes)
    nbvariables = len(countVariables(lignes))
    pourcentage = round(compteur/nbvariables)*100
    note=10-(0.5*compteur)
    if note >=0:
        note=note
    else:
        note = 0
    return("Variables appelées-Evaluation de l'appel des variables-variables non utilisées+variables utilisées-"+str(pourcentage)+"-Note:"+str(note)+"-|")

