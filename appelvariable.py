from trouve_fonction import count_fonction
from test_variables import countVariables 

def numlignevarglo(lignes):             #lignes=fichier texte contenant toutes les lignes du code
    #va récupérer les lignes en dehors des fonctions
    L=count_fonction(lignes)
    var=[]
    numligne= [i for i in range(1,len(lignes))]
    for i in range (len(lignes)):    #on va parcourir toutes les lignes du code
        (deb,fin)=(L[i]['start'],L[i]['fin'])    #on récupère la ligne de début et de fin de chaque fonction
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
        
def varglobefore(i,lignes):
#prend en argument les lignes et i un indice et renvoie la liste des variables globales qui aparaissent avant cet indice
    L=varglobal(lignes)
    T=[]
    for k in L:
        if k[1]<i:
            T.append(varglobal[k][0])
    return T

def textefonctions(lignes):             
    #renvoie une liste dont les éléments sont le texte des différentes fonctions
    listedico 

def appelvar (lignes):                          #lignes=fichier texte contenant toutes les lignes du code
    #regarde si une variable a été utilisée 
    fonctions=[]                                #on créé une liste dont chaque élément est une fonction 
    fonction=[]
    varglo= varglobal(lignes)
    var=[]
    for ligne in lignes:                            
        if "def" not in ligne:              
            fonction=fonction+ligne
        else:
            fonctions.append(fonction)
            fonction=[ligne]
    for fonction in fonctions :
        vars= countVariables(fonction)                  #fonction qui renvoie les variables dans une liste
        for var in vars:
            count               

fp=open('event_candidate_a.rb.rb','r')
L=fp.readlines()
print(L)
#print(numlignevarglo(L))


                       
