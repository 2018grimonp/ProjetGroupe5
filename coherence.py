import re   #module pour utiliser les expressions reguliere  faire pip install re

"""On considere que l'on a en entree un tableau contenant tout les noms des variables contenus dans un code.
Ce tableau a ete obtenu avec le programme test_variable.
On considere ici les convention de nommage CamelCase et python.
On separe d'abord les mots dans un nom de variable, puis on verifie que les mots existent (et que l'ensemble veut bien dire qqch)"""


"""le premier programme renvoi un tableau contenant tout les mots de la langues francaise"""
l="liste.de.mots.francais.frgut.txt"

def readLines(path):  # retire les '/n' d'un fichier texte 
    L=[]
    with open(path,'r') as fp:
        for line in fp:
            line=line.replace('\n', '')
            L.append(line)
    return L


"""c'est deux programmes renvoi un tabelau contenant les different nom en minuscules des noms des variables"""
def nom_underscore(str):  #str=le nom d'UNE variable
    return str.split("_")


#les deux fonctions definies icic servent pour la fonction camel_case
def il_y_a_maj(str):
    est_maj=False
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if str.find(i)!=-1:
            est_maj=True
    return est_maj

def inverse(str):
    inv=str[-1]
    str=str[:-1]
    while len(str)>0:
        inv+=str[-1]
        str=str[:-1]
    return inv

"""re.match(regex, str) retourn None si il n'y a pas de match entre la regex et la string"""
def nom_camel_case(str): #str=le nom d'UNE variable
    noms=[]
    if re.match("^[A-Z]$",str)!=None:     #on test s'il y a des majuscules
        return [str]
    else:
        nom=str[-1].lower()
        str=str[:-1]
        while len(str)>1:
            while il_y_a_maj(nom)==False:  #il n'y a pas de majuscules dans le nom
                #print (nom)
                if len(str)==1:            #s'assurer que la string est non vide
                    nom+=str
                    noms.append(inverse(nom).lower())
                    return noms
                else:
                    nom+=str[-1]
                    str=str[:-1]
            noms.append(inverse(nom).lower())              #on reinitiallise des qu'une maj est rencontre
            nom=str[-1].lower()
            str=str[:-1]
    return noms

"""programme final"""

def nom_coherent(list_str):    #on prend en argument la liste des noms des variables utiles
    tout_les_noms_sont_cohérents=True
    for str in list_str:
        if str.find("_")!=-1:
            nom_tab=nom_underscore(str)   #tableau contenant les noms de la variables (ex: "cornichon_vert" => ["cornichon","vert"])
        else:
            nom_tab=nom_camel_case(str)
        len_nom_tab=len(nom_tab)
        count=0
        nom_exist=[]
        for nom in nom_tab:
            for word in readLines(l):
                if nom ==word:
                    count+=1
        if count!=len_nom_tab:
            print("le nom de la variable " + str + " " +"n'est pas un choix judicieux. ")
            tout_les_noms_sont_cohérents=False
    if tout_les_noms_sont_cohérents==True:
        return print("Tes variables ont des noms bien choisi !")
    else:
        return print("Tes choix de noms de variables sont nuls !")
  

#print(nom_coherent(["cornihon_vert","CornichonVert"]))
#print(nom_coherent(["cdjiezqnfui_vert","ChuihuiVert"]))
