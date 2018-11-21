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
    return(ListeLongeurFonction)

#omg c'est trop cool

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
    return(True)
