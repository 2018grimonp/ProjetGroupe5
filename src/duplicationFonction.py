import trouve_fonction
import commentaires
import checkIndentation

"""
on considère qu'on as une base de donnèes de fonction classique sous forme de liste de ligne
"""
code_controle=
"""
le code à analyser est Code (liste de string)
"""
def controle_duplication(Code,precision):
    Code=checkIndentation.retirerIndentation(commentaires.retirerCom(Code)) #on enlève indentation et commentaires
    Code=cutVariable(Code)                                                  #on enlève les variables
    similitude_fonctions=[]
    fonctions=trouve_fonction.count_fonction(Code)
    for num_fonction in range(len(fonctions)):
        similitude_fonctions.append(controle_duplicat_fonction(Code[fonctions["start"]+1:fonctions["end"]],precision))

"""
controle si une fonction est semblable à d'autres,
renvois une liste de dictionniare qui indique:
    'ligneControle' : où ce trouve la fonction dans le texte de controle
    'pourcentage' : le pourcentage de similitude avec cette fonction
"""

def controle_duplicat_fonction(fonction,precision):
    similitude=[]       #dico (cf explication en haut)
    l=len(fonction)
    indice_controle,indice_fonction=0,0
    pourcentage=0
    while indice_controle<len(code_controle) :                                                          #parcour, le code de controle
        prec=pourcentage_similitude_ligne(fonction[indice_fonction],code_controle[indice_controle])     #controle si les lignes sont semblable
        if prec>precision :                                         #si oui controle la ligne suivante ecc...
            pourcentage=+prec/l
            indice_fonction+=1
            if indice_fonction==l :
                similitude.append({"pourcentage": pourcentage ,"ligneControle" : indice_controle-l })
                indice_fonction=0
                pourcentage=0
        indice_controle+=1
    return (similitude)


def pourcentage_similitude_ligne(ligne1,ligne2):
    l1,l2 =len(ligne1),len(ligne2)
    if l1>l2 :                      #on ajuste la longueur des lignes
        for k in range(l1-l2):
            ligne2=ligne2+" "
            l=l1
    else :
        for k in range(l2-l1):
            ligne1=ligne1+" "
            l=l2
    same=0
    for i in range(l):              #on compte les caractère semblable
        if ligne2[i]==ligne1[i]:
            same+=1
    return(same/l*100)              #on retourne le pourcentage de caractères semblable

def print_resultats_similitude(Code,precision):
