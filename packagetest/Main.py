def readLines(l):  # retire les '\n' d'un fichier texte 
    L=[]
    with open(l,'r') as fp:
        for line in fp:
            line=line.replace('\n', '')
            L.append(line)
    print(L)
    return L

#print ('What is the file you want to analyse?')

#t=input()           #on rentre le fichier que l'on veut manipuler

#T=readLines(t)

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




