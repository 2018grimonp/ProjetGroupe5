lines = ['Une ligne qui sert à rien', '#Un commentaire normal', 'une ligne inutile #avec un com à la fin', '=begin un commentaire en block', 'ca continue', '=end']
import numpy as np
from textblob import TextBlob

def fichierLecture():
    """
    Ouvre le fichier event_candidate_a.rb.rb, juste pour pouvoir tester les fonctions (à virer)
    :return: la liste des lignes du fichier
    """
    try:
        fichier = open("./test.rb", "rt")
        ligneListe = fichier.readlines()
        return ligneListe
    except IOError:
        print("Erreur fichier")

#print(fichierLecture())

def commentsHashtag(lines):
    """
    Donne les commentaires unitaires
    :param lines: le code représenté par une liste de lignes
    :return: un dico avec la liste des commentaires (sans le #) associée à la ligne du com
    """
    commentDico = {}
    #On itère sur chaque ligne
    for lineNumber in range(len(lines)):
        i = 0
        isComment = False
        comment = ''
        while i < len(lines[lineNumber]) and not isComment:

            #On détècte un commentaire dès qu'il y a un #
            if lines[lineNumber][i] == '#':
                isComment = True
            i += 1

        #Le commentaire correspond à la fin de la ligne
        if isComment:
            comment = lines[lineNumber][i:]
        if comment != '':
            commentDico[lineNumber] = [comment, len(comment)]
    return commentDico

#print(commentsHashtag(lines))

def commentBlocks(lines):
    """
    Donne les commentaires en block (=begin ... commentaire ... =end)
    :param lines: le code représenté par une liste de lignes
    :return: un dico avec le commentaire en block associé au numéro de la première ligne de commentaire
    """
    commentDico = {}
    isBlock = False
    #On regarde à chaque ligne si il y a le mot "=begin"
    for lineNumber in range(len(lines)):
        #On détecte le debut du commentaire par le '=begin'
        if lines[lineNumber][:6] == '=begin':
            isBlock = True
            block = lines[lineNumber][6:]
            blockLine = lineNumber
            continue

        #On enregistre les lignes de commentaires jusqu'à '=end'
        if isBlock and lines[lineNumber][:4] != '=end':
            block += lines[lineNumber]

        #On enregistre le commentaire lorsqu'on tombe sur un '=end'
        if isBlock and lines[lineNumber][:4] == '=end':
            isBlock = False
            commentDico[blockLine] = [block, len(block)]

    return commentDico

#print(commentBlocks(lines))

def commentCount(lines):
    """
    Donne un couple (nombre de lignes de com, {ligne: [commentaire, nb de carac]})
    :param lines: le code représenté par une liste de lignes
    :return: le fameux couple
    """
    dicoHash = commentsHashtag(lines)
    dicoBlock = commentBlocks(lines)
    count = len(dicoHash) + len(dicoBlock)
    commentDico = {}
    for key in dicoHash:
        commentDico[key] = dicoHash[key]
    #Je rajoute les blocks après au cas où ya un # dans un block
    for key in dicoBlock:
        commentDico[key] = dicoBlock[key]
    return count, commentDico

#print(commentCount(lines))

def detectCom(line):
    """
    Détecte si il y a un commentaire sur cette ligne
    :param line: la fameuse ligne
    :return: 0 si la ligne ne comporte pas de commentaire
             i+1 si il y a un # à l'indice i de la ligne
             -1 si c'est un =begin
             -2 si c'est un =end
    """
    if line[:6] == '=begin':
        return -1
    if line[:4] == '=end':
        return -2
    for i in range(len(line)):
        if line[i] == '#':
            return i+1
    return 0

def retirerCom(lines):
    """
    On retire les commentaires du script
    :return: la nouvelle liste nettoyée
    """
    #On retire les commentaires
    newLines = []
    isBlock = False
    for line in lines:
        test = detectCom(line)
        if test == 0:
            if not isBlock:
                newLines.append(line)
            pass
        if test > 0:
            if not isBlock:
                newLines.append(line[:test-1])
        if test == -1:
            isBlock = True
        if test == -2:
            isBlock = False
    #Et on renvoie la nouvelle liste de lignes
    return newLines

#print(fichierLecture())
#print(retirerCom(lines))

def analyseCom(lines):
    """
    donne des données intéressantes sur le fichier texte
    :return: liste des commentaires, ratio caractères commentés, ratio lignes commentées
    """
    caracNumber = sum([len(line) for line in lines]) #nombre de caractères en tout
    linesNumber = len(lines) #nombre de lignes du fichier
    linesList = [0 for a in range(linesNumber)]
    com = commentCount(lines)[1]
    comCount = commentCount(lines)[0]

    #Enregistre le nombre de commentaires par ligne
    for lineNumber in range(linesNumber):
        if lineNumber in com.keys():
            linesList[lineNumber] += com[lineNumber][1]

    #Enregistre le nombre de caractères dédiés aux commentaires
    comCarac = 0
    for ligne in com.keys():
        comCarac += com[ligne][1]

    #Enregistre le nombre de lignes où il y a un commentaire
    commentLinesNumber = len([i for i in linesList if i != 0])

    return linesList, comCarac/caracNumber, commentLinesNumber/linesNumber, comCount

#print(analyseCom(lines))

def printCom(lines):
    analyse = analyseCom(lines)
    ratio = ratioFrancais(lines)
    print('-------- Nombre de commentaires --------')
    if analyse[3] == 0:
        print('Le fichier n\'est pas commenté')
    elif analyse[3] == 1:
        print('Le fichier comporte un seul commentaire')
    else:
        print('Le fichier comporte '+str(analyse[3])+' commentaires.')
    print('-------- Pourcentage de caractères dédiés aux commentaires --------')
    print(str(int(analyse[1]*10000)/100)+'%')
    print('-------- Pourcentage de lignes dédiées aux commentaires --------')
    print(str(int(analyse[2]*10000)/100)+'%')
    print('-------- Proportion de mots francais --------')
    print('Mots fréquents : '+str(ratio[0])+' -- Mots peu utilisés : '+str(ratio[1]))

#print(commentCount(fichierLecture()))

def howCommented(lines):
    """
    Donne des infos par rapport à la répartition des commentaires
    :param lines: le code représenté par une liste de lignes
    :return: False si le code n'est pas commenté
             True s'il est commenté
             et deux couples (moy, stDevCom) et (caracRatio, linesRatio)
             moy = moyenne de caracètres de commentaire par ligne
             stDevCom = écart type
             caracRatio = pourcentage de caractères de commentaire
             linesRatio = pourcentage de lignes de commentaires
    """
    count = commentCount(lines)
    analyse = analyseCom(lines)
    comLines = np.array(analyse[0])
    if count[0] == 0:
        return False, (0, 0), (0,0)
    else:
        moy = sum(comLines)/len(comLines)
        moySq = sum(comLines**2)/len(comLines)
        varCom = moySq - moy**2
        stDevCom = np.sqrt(varCom)
        return True, (moy, stDevCom), (analyse[2], analyse[1])

def commentsWords(lines):
    """
    Donne les mots utilisés dans les commentaires
    :param lines: le code représenté par une liste de lignes
    :return: un dico des mots fréquemment utilisés avec leur fréquence
             une liste des mots utilisés une seule fois
    """
    comments = [comment[0] for comment in list(commentCount(lines)[1].values())]
    commentAll = ''
    for comment in comments:
        commentAll += comment
    commentAll = TextBlob(commentAll)
    dicoFrequent = {}
    notFrequentList = []
    wordList = commentAll.words.lemmatize()
    for word in wordList:
        count = commentAll.words.count(word)
        if count > 1:
            dicoFrequent[word.lower()] = commentAll.words.count(word)
        else:
            notFrequentList.append(word)
    return dicoFrequent, notFrequentList

def isFrancais(word, dictionaire):
    return word.lower() in dictionaire

def ratioFrancais(lines):
    """
    Donne le ratio de mots francais dans les commentaires
    :param lines: le code représenté par une liste de lignes
    :return: un tuple contenant les fameux ratios (mots fréquents, mots moins fréquents)
    """
    frequent, notFrequent = commentsWords(lines)
    numberFrFreq = 0
    numberFrNFreq = 0
    try:
        fichier = open('./liste.de.mots.francais.frgut.txt', 'r')
        mots = [mot.replace('\n', '') for mot in fichier.readlines()]
        motsDecode =[mot.encode('iso-8859-1').decode('utf8') for mot in mots]
        for mot in frequent.keys():
            if isFrancais(mot, motsDecode):
                numberFrFreq += frequent[mot]
        for mot in notFrequent:
            if isFrancais(mot, motsDecode):
                numberFrNFreq +=1
        return numberFrFreq/sum(frequent.values()), numberFrNFreq/len(notFrequent)
    except IOError:
        print("La liste des mots francais n'est pas là")

#print(wellCommented(lines)
#print(commentsWords(fichierLecture()))
printCom(lines)
