import matplotlib.pyplot as plt
def fichierLecture():
    """
    Ouvre le fichier event_candidate_a.rb.rb, juste pour pouvoir tester les fonctions
    :return: la liste des lignes du fichier
    """
    try:
        fichier = open("../test_candidats/event_candidate_a.rb.rb", "rt")
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


#print(commentsHashtag(fichierLecture()))


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
        #On enregistre les lignes de commentaires jusqu'à '=end'
        if isBlock and lines[lineNumber][:4] != '=end':
            block += lines[lineNumber]

        #On enregistre le commentaire lorsqu'on tombe sur un '=end'
        if isBlock and lines[lineNumber][:4] == '=end':
            isBlock = False
            commentDico[blockLine] = [block, len(block)]

        #On détecte le debut du commentaire par le '=begin'
        if lines[lineNumber][:6] == '=begin':
            isBlock = True
            block = lines[lineNumber][6:]
            blockLine = lineNumber
            pass
    return commentDico


#print(commentBlocks(fichierLecture()))


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

#print(commentCount(fichierLecture()))

def detectCom(line):
    """
    Détecte si il y a un commentaire sur cette ligne
    :param line: la fameuse ligne
    :return: 0 si la ligne ne comporte pas de commentaire
             i si il y a un # à l'indice i de la ligne
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
    newLines = []
    isBlock = False
    for line in lines:
        test = detectCom(line)
        if test == 0:
            if not isBlock:
                newLines.append(line)
            pass
        if test > 0:
            newLines.append(line[:test-1])
        if test == -1:
            isBlock = True
        if test == -2:
            isBlock = False
    return newLines

#print(fichierLecture())
#print(commentCount(retirerCom(fichierLecture())))

def analyse(lines):
    caracNumber = sum([len(line) for line in lines])
    linesNumber = len(lines)
    linesList = [0 for a in range(linesNumber)]
    com = commentCount(lines)[1]
    print(com)
    for lineNumber in range(linesNumber):
        if lineNumber in com.keys():
            linesList[lineNumber] += com[lineNumber][1]
    return linesList

plt.plot(analyse(fichierLecture()))
plt.show()
