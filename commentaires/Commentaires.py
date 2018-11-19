from textblob import TextBlob

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
            commentDico['ligne ' +str(lineNumber)] = [comment, len(comment)]
    return commentDico


print(commentsHashtag(fichierLecture()))


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
        if isBlock and lines[lineNumber][:4] != '=end':
            block += lines[lineNumber]
        #On enregistre les lignes de commentaires jusqu'à '=end'
        if isBlock and lines[lineNumber][:4] == '=end':
            isBlock = False
            commentDico['ligne '+str(blockLine)] = [block, len(block)]
        #On enregistre le commentaire lorsqu'on tombe sur un '=end'
        if lines[lineNumber][:6] == '=begin':
            isBlock = True
            block = lines[lineNumber][6:]
            blockLine = lineNumber
            pass
    return commentDico


print(commentBlocks(fichierLecture()))


def commentCount(lines):
    """
    Donne un couple (nombre de com, {'ligne': [commentaire, nb de carac]})
    :param lines: le code représenté par une liste de lignes
    :return: le fameux couple
    """
    dicoHash = commentsHashtag(lines)
    dicoBlock = commentBlocks(lines)
    count = len(dicoHash) + len(dicoBlock)
    commentDico = {}
    for key in dicoHash:
        commentDico[key] = dicoHash[key]
    for key in dicoBlock:
        commentDico[key] = dicoBlock[key]
    return count, commentDico

print(commentCount(fichierLecture()))
