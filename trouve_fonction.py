#code à analyser
open=["if","while","for","do","class"]

Code = ["hello","def gilbert","end"]    #liste de ligne (str)

ListeLongeurFonction=[] #donne une liste des n fonctions avec la longeur de chaque liste
           #indique le nombre de parentaises ouverte

def ligne_open(k):
    for word in open:
        if word in Code[k].slit(" "):
            return True
    return False

def count_fonction():
    open_count=0
    fonction_open=False
    def_open=-1
    for k in range(len(Code)):
        if Code[:3]=="def" :
            #test si une fonction est déjà ouverte
            if fonction_open :
                return("Erreur fonction lingne "+str(k))
            else :
                fonction_open=True
            ListeLongeurFonction.append(k)
            def_open=open_count
            open_count+=1
        if ligne_open(k) :
            open_count+=1
                                #regarde si ont ferme
        if Code[:3]=="end" :
            open_count-=1
            if open_count== def_open :
                ListeLongeurFonction[-1]=k-ListeLongeurFonction[-1]
    return(ListeLongeurFonction)

