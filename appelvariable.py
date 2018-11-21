def appelvar (lignes):          #lignes=fichier texte contenant toutes les lignes du code
    fonctions=[]
    fonction=[lignes.pop([0])]
    for ligne in lignes:
        if "def" not in ligne:
            fonction=fonction+ligne
        else:
            T.append(fonction)
            fonction=[ligne]
            
L=[0,2,3]
l=L.pop(1)
print (l)                
