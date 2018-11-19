#liste de commande qui ouvre des actions
open=["if","while","for","do","class"]

#code à analyser
Code = ["hello","def gilbert","end"]    #liste de ligne (str)

ListeLongeurFonction=[] #donne une liste des n fonctions avec la longeur de chaque liste
           #indique le nombre de parentaises ouverte

def ligne_open(k):      #controlle si la ligne ouvre des commande
    for word in open:
        if word in Code[k].slit(" "):
            return True
    return False

def count_fonction():
    open_count=0
    fonction_open=False
    def_open=-1
    for k in range(len(Code)):      #parcour le texte
        if Code[:3]=="def" :
            if fonction_open :                  #test si une fonction est déjà ouverte
                return("Erreur fonction lingne "+str(k))
            else :
                fonction_open=True
            ListeLongeurFonction.append(k)      #sauvegarde l'indice de début de la fonction
            def_open=open_count
            open_count+=1
        if ligne_open(k) :      #controle si la ligne ouvre des commandes
            open_count+=1
        if Code[:3]=="end" :    #controle si la ligne ferme des commandes
            open_count-=1
            if open_count== def_open :
                ListeLongeurFonction[-1]=k-ListeLongeurFonction[-1]-1   #calcul la longueur de la fonction (def et end exclus)
    return(ListeLongeurFonction)

#omg c'est trop cool

