import duplicationFonction
import duplicationInterne

def creation_string(code,codeControle,precision):
    donnees=duplicationFonction.retuour_resresultats_similitude(code,precision,codeControle)
    copies_percent=donnees[0]/donnees[1]
    graph="Fonction copié-donne le nombre de fonctions suceptible d'e^tre fraudé (avec une précision minimale de "+str(precision)+"% -fonction originale+fonctions copiées-"+str(copies_percent)+"-Multiplicateur de note: "+str(copies_percent/10)+"/10-|"
    return (graph)
