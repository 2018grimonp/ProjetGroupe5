def initial(l):  # retire les '/n' d'un fichier texte 
    L=[]
    with open(l,'r') as fp:
        for line in fp:
            line=line.replace('/n', '')
            L.append(line)
    return L

print ('What is the file you want to analyse?')

t=input()           #on rentre le fichier que l'on veut manipuler

T=initial(t)

