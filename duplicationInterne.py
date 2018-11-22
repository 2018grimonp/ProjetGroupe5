import trouve_fonction
import commentaires
import checkIndentation
import duplicationFonction

"""
On spot les fonctions et les variable qui ont le me^me nom #pas cool
"""

"""
cette fonction trouve les fonction de nom identique au sein du code et donne si les code associer sont effectivement identique
output: fonction["status"]=[(id fonction de me^me nom, realtion), (...), ...]
"""
#On considère que Code ne possède plus d'indentations ni de commentaire
def double_fonction_meme_nom(Code):
    liste_fonction=trouve_fonction.count_fonction(Code)
    for i in range(len(liste_fonction)-1) :
        for j in range(i+1,len(liste_fonction)):
            if liste_fonction[i]["nom"]==liste_fonction[j]["nom"] :
                liste_fonction[i]["copie_status"].append((j,ressamblance_fonction(Code[liste_fonction[i]["start"]+1:liste_fonction[i]["end"]],Code[liste_fonction[j]["start"]+1:liste_fonction[j]["end"]])))
                liste_fonction[j]["copie_status"].append((i,ressamblance_fonction(Code[liste_fonction[i]["start"]+1:liste_fonction[i]["end"]],Code[liste_fonction[j]["start"]+1:liste_fonction[j]["end"]])))
    return(liste_fonction)

"""
input: 2 fonctions (liste de strings)
output: le pourcentage de ressemblance des 2 fonctions
"""
def ressamblance_fonction(f1,f2):
    l1,l2 =len(f1),len(f2)
    if l1>l2 :                      #on ajuste la longueur des fonction
        for k in range(l1-l2):
            f2=f2+[]
        l=l1
    else :
        for k in range(l2-l1):
            f1=f1+[]
        l=l2
    same=0
    for k in range(len(f1)):            #on calcule les similitude
        same+=duplicationFonction.pourcentage_similitude_ligne(f1[k],f2[k])
    return(same/l)

