def test_variables(lines): #lines=tableau de lignes
    """entré: une liste de lignes (sans les '/n')
       sortie: le nombre de variable dans le code, un tableau du nom de cahque variables"""
    nombre_variables=0
    tableau_variables=[]   #pour stocker les variables
    for line in lines:
        if line.find("=")!=-1:
            #print(line)
            tableau_avant_apres=line.split("=")    #on separe la chaine avant et apres le egale
            #print(tableau_avant_apres)
            string_avant=tableau_avant_apres[0]
            #print(string_avant)
            tableau_avant=string_avant.split(" ") #on recuper le nom de la variable, qui se trouve dans la derniere case du tableau
            #print(tableau_avant)
            tableau_variables.append(tableau_avant_apres[-1])
    tableau_variables_sans_doublons=set(tableau_variables)
    #print(tableau_variables_sans_doublons)
    nombre_variables=len(tableau_variables_sans_doublons)
    return nombre_variables, tableau_variables_sans_doublons


def print_test_variable(lines):
    """renvoi toutes les noms des variables qui sont utlisiées ainsi que leur nombre.
une variable sera consideree comme utilisee si elle apprait deux fois dans le code"""
    result=test_variables(lines)   #c'est un tuples, (int, list)
    variables_utiles=[]
    for var in result[1]:
        count=0
        for line in lines:
            list_line=line.split(" ")
            for word in list_line:
                if var==word:
                    count+=1
        if count>2:
            variables_utiles.append(var)
        nb_variables_utiles=len(variables_utiles)
        str_variables_utiles=",".joint(variables_utiles)
        return print ("Il y a "+str(nb_variables_utiles)+ ". Elle s'appelle " + str_variables_utiles +" .")

