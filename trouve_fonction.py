import random as rd
#liste de commande qui ouvre des actions
open=["if","while","for","do","class"]


#code à analyser
Code1 = ["hello","def gilbert():","    lol","end","def bilibili(nhassah,aidj):","f","   if lol do","  end","end"]    #liste de ligne (str)

ListeLongeurFonction=[] #donne une liste des n fonctions avec la longeur de chaque liste
           #indique le nombre de parentaises ouverte

def ligne_open(k,Code):      #controlle si la ligne ouvre des commande
    for word in open:
        if word in Code[k].split(" "):
            return True
    return False

def count_fonction(Code):
    ListeLongeurFonction=[]
    open_count=0
    fonction_open=False
    def_open=-1
    for k in range(len(Code)):      #parcour le texte
        if Code[k][:3]=="def" :
            if fonction_open :                  #test si une fonction est déjà ouverte
                return("Erreur fonction lingne "+str(k))
            else :
                fonction_open=True
            ListeLongeurFonction.append({"start":k}) #sauvegarde l'indice de début de la fonction
            ListeLongeurFonction[-1]["nom"]=Code[k][4:].split("(")[0]
            def_open=open_count
            open_count+=1
        if ligne_open(k,Code) :      #controle si la ligne ouvre des commandes
            open_count+=1
        if "end" in Code[k].split(" ") :    #controle si la ligne ferme des commandes
            open_count-=1
            if open_count<0 :
                print(ListeLongeurFonction)
                return("end not open ligne "+ str(k))
            if open_count== def_open :
                ListeLongeurFonction[-1]["end"]=k
                ListeLongeurFonction[-1]["longueur"]=k-ListeLongeurFonction[-1]["start"]-1   #calcul la longueur de la fonction (def et end exclus)
                fonction_open=False
                def_open=-1
    return(ListeLongeurFonction)

#omg c'est trop cool
print(count_fonction(Code1))

def printFonction(Code):
    fonctions=count_fonction(Code)
    if type(fonctions)!= list :
        print(fonctions)
        return(False)
    if len(fonctions)==0 :
        print("omg ce candidat n'utilise pas de fonctions")
        return(False)
    l_moyenne,l_min,l_max=0,fonctions[0]["longueur"],fonctions[0]["longueur"]
    print("nom des fonctions :")
    for num_fonction in range(len(fonctions)):
        #print("fonction "+str(num_fonction))
        print(str(num_fonction)+". "+fonctions[num_fonction]["nom"])
        #print("longueur : "+str(fonctions[num_fonction]["longueur"])+"\n")
        l_moyenne+=fonctions[num_fonction]["longueur"]
        if fonctions[num_fonction]["longueur"]<l_min :
            l_min=fonctions[num_fonction]["longueur"]
        if fonctions[num_fonction]["longueur"]>l_max :
            l_max=fonctions[num_fonction]["longueur"]
    print ("\nla longueur moyenne est : "+str(l_moyenne/len(fonctions)))
    print ("la longueur minimal est : "+str(l_min))
    print ("la longueur maximal est : "+str(l_max))
    print ("le nom de fonction le plus stylé est : "+fonctions[rd.randint(0,len(fonctions)-1)]["nom"])
    point = points(fonctions, l_moyenne/len(fonctions))
    graphique = 'Fonctions-'+point[1]+'-Lignes de fonctions+Reste des lignes-'+str(int(l_moyenne/len(Code)*100))+'-Note : '+str(point[0])+'/10-|'
    return(graphique, l_moyenne)

def points(fonctions, l_moyenne):
    '''
    Donne le nombre de points obtenus quant à l'écriture des fonctions
    :param fonctions: la liste des fonctions du code
    :param l_moyenne: la longueur moyenne d'une fonctions
    :return: la note sur 10 ainsi qu'un commentaire associé
    '''
    L = len(fonctions)
    if L == 0:
        return 0, 'Ce candidat n\'utilise pas de fonctions'
    else:
        if l_moyenne < 2:
            note = 1
            commentaire = 'Les fonctions sont trop petites'
        elif l_moyenne < 5:
            if L < 5:
                note = 5
                commentaire = 'Les fonctions sont petites et il y en a pas assez'
            elif L < 20:
                note = 9
                commentaire = 'Les fonctions sont très satisfaisantes'
            else:
                note = 2
                commentaire = 'Il y a trop de fonctions'
        elif l_moyenne < 15:
            if L < 2:
                note = 4
                commentaire = 'Il y a pas assez de fonctions mais elles ont une taille raisonnable'
            elif L < 5:
                note = 8
                commentaire = 'Les fonctions sont de taille raisonnable, il y en a assez'
            elif L < 20:
                note = 10
                commentaire = 'Le fonctions sont bien gérées'
            else:
                note = 3
                commentaire = 'Il y a trop de fonctions'
        else:
            if L < 5:
                note = 2
                commentaire = 'Les fonctions sont trop grosses, il y en a trop peu'
            elif L < 20:
                note = 4
                commentaire = 'Les fonctions sont trop grosses mais il y en pas mal'
            else:
                note = 1
                commentaire = 'Les fonctions sont trop grosses, il y en a beaucoup trop !'
    return note, commentaire

print(printFonction(Code1))
