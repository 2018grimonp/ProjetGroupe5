import re

def print_variables(lines): #lines=tableau de lignes
    """entré: une liste de lignes (sans les '/n')
       sortie: le nombre de variable dans le code, un tableau du nom de cahque variables"""
    nombre_variables=0
    tableau_variables=[]   #pour stocker les variables
    for line in lines:
        if line.find("=")>0:
            #print(line)
            tableau_avant_apres=line.split("=")    #on separe la chaine avant et apres le egale
            #print(tableau_avant_apres)
            string_avant=tableau_avant_apres[0]
            #print(string_avant)
            tableau_avant=string_avant.split(" ") #on recuper le nom de la variable, qui se trouve dans la derniere case du tableau
            print(tableau_avant[-1])
            if re.match("^[A-Za-z]$",tableau_avant[-1])!=None:  #s'il y a pas un espace avant le =
                tableau_variables.append(tableau_avant[-1])
            else:                                             #s'il y a un espace avant le =
                tableau_avant.pop()
                tableau_variables.append(tableau_avant[-1])
    tableau_variables_sans_doublons=set(tableau_variables)
    print(tableau_variables_sans_doublons)
    nombre_variables=len(tableau_variables_sans_doublons)
    str_variables_utiles=",".join(tableau_variables_sans_doublons)
    return print ("Il y a "+str(nombre_variables)+ ". Elles s'appellent " + str_variables_utiles +" .")



