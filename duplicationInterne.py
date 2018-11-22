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
def double_fonction(Code):
    liste_fonction=trouve_fonction.count_fonction(Code)
    for i in range(len(liste_fonction)) :
        for j in range(i+1,len(liste_fonction)):
            if liste_fonction[i]["nom"]==liste_fonction[j]["nom"] :
                liste_fonction[i]["copie_status"].append((j,ressamblance_fonction()))

def ressamblance
