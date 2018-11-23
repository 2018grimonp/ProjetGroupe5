import trouve_fonction
import commentaires
import checkIndentation
import trouve_variables

"""
on considère qu'on as une base de donnèes de fonction classique sous forme de liste de ligne
"""

"""
le code à analyser est Code (liste de string)
input: code et code_controle sont 2 listes de strings  
    precision définie avec quelle précision on considère 2 codes identique
output: liste de dictionnaire qui pour chaque fonction de code donne les correspondente de code_controle
"""

def controle_duplication(Code,precision,code_controle):
    Code=checkIndentation.retirerIndentation(commentaires.retirerCom(Code))                     #on enlève indentation et commentaires
    code_controle=checkIndentation.retirerIndentation(commentaires.retirerCom(code_controle))
    Code=trouve_variables.snailVariables(Code,trouve_variables.countVariables(Code))           #on enlève les variables
    code_controle=trouve_variables.snailVariables(code_controle,trouve_variables.countVariables(code_controle))
    similitude_fonctions=[]
    fonctions=trouve_fonction.count_fonction(Code) #trouve les fonctions de code
    for num_fonction in range(len(fonctions)):
        similitude_fonctions.append(controle_duplicat_fonction(Code[fonctions[num_fonction]["start"]+1:fonctions[num_fonction]["end"]],precision,code_controle))
    return(similitude_fonctions)

"""
controle si une fonction est semblable à d'autres,
renvois une liste de dictionniare qui indique:
    'ligneControle' : où ce trouve la fonction dans le texte de controle
    'pourcentage' : le pourcentage de similitude avec cette fonction
"""

def controle_duplicat_fonction(fonction,precision,code_controle):
    similitude=[]       #dico (cf explication en haut)
    l=len(fonction)
    indice_controle,indice_fonction=0,0
    pourcentage=0
    while indice_controle<len(code_controle) :                                                          #parcour, le code de controle
        prec=pourcentage_similitude_ligne(fonction[indice_fonction],code_controle[indice_controle+indice_fonction])     #controle si les lignes sont semblable
        if prec>precision :                                         #si oui controle la ligne suivante ecc...
            pourcentage+=prec/l
            indice_fonction+=1
            if indice_fonction==l :
                similitude.append({"pourcentage": pourcentage ,"ligneControle" : indice_controle })
                indice_fonction=0
                pourcentage=0
                indice_controle+=1
        else :
            indice_fonction=0
            indice_controle+=1
    return (similitude)

"""
input: 2 strings
output: pourcentage de similitude des 2 strings
"""

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

"""
input: 2 codes (tableau de strings) et une précision (float de 0 à 100)
output: print des données générales sur les duplicat entre les 2 input
"""

def print_resultats_similitude(Code,precision,code_controle):
    Liste_duplicat=controle_duplication(Code,precision,code_controle)
    s,pourcentage_tot=0,0
    for k in Liste_duplicat :
        if k!=[] :
            s+=1
            pourcentage_tot+=max_percent(k)
    pourcentage_tot=pourcentage_tot/len(Liste_duplicat)
    print(str(s)+" fonctions pourraient e^tre copié")
    print("le pourcentage di similitude moyen avec d'autres codes est : "+str(pourcentage_tot)+"%")

def retuour_resresultats_similitude(Code,precision,code_controle):
    Liste_duplicat=controle_duplication(Code,precision,code_controle)
    s,pourcentage_tot=0,0
    for k in Liste_duplicat :
        if k!=[] :
            s+=1
            pourcentage_tot+=max_percent(k)
    pourcentage_tot=pourcentage_tot/len(Liste_duplicat)
    return(s,len(Liste_duplicat),pourcentage_tot)
"""
input: La liste des dico qui représente les similitude d'une fonction avec le code_controle
output: retourne le pourcentage maximale de ressemblance avec une autre fonction
"""
def max_percent(Liste_dico):
    max=Liste_dico[0]["pourcentage"]
    for k in Liste_dico:
        if k["pourcentage"]>=max :
            max=k["pourcentage"]
    return(max)



