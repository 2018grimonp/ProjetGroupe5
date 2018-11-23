from trouve_fonction import count_fonction
from trouve_variables import countVariables

def numlignevarglo(lignes):             #lignes=fichier texte contenant toutes les lignes du code
    #va récupérer les lignes en dehors des fonctions
    L=count_fonction(lignes)
    var=[]
    numligne= [i for i in range(1,len(lignes))]
    for i in range (len(lignes)):    #on va parcourir toutes les lignes du code
        (deb,fin)=(L[i]['start'],L[i]['end'])    #on récupère la ligne de début et de fin de chaque fonction
        for k in range (deb,fin+1):
            numligne.pop(k)                 #on retire les indices des lignes où il y a une fonction
    return numligne

def varglobal(lignes):
    #renvoie les variables globales et les indices des lignes où elles apparaissent
    L=numlignevarglo(lignes)
    vars=[]
    for i in L:
        var= countVariables(lignes[i])                                  #appel fonction pour récupérer la variable dans la ligne i de lignes
        vars.append([var[0],i])                                         #var= un tableau avec comme seul élément une variable
    return vars
        
def varglobefore(i,lignes):   #seule fonction qui marche....
#prend en argument les lignes et i un indice et renvoie la liste des variables globales qui aparaissent avant cet indice
    L=varglobal(lignes)
    T=[]
    for k in L:
        if k[1]<i:
            T.append(varglobal[k][0])
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
    for i in L :    
        vars= countVariables(L[i][1])                    #vars = les variables dans la ième fonction 
        vars= vars + varglobefore(L[i][0])                #on rajoute les variables globales créées avant la fonction 
        for var in vars:
            if vars.count(var) ==1:
                compteur+=1
    return compteur                   
