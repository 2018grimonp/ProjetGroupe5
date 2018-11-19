from textblob import TextBlob

def fichierLecture():
    try:
        fichier = open("../test_candidats/event_candidate_a.rb.rb", "rt")
        ligneListe = fichier.readlines()
        return ligneListe
    except IOError:
        print("Erreur fichier")

#print(fichierLecture())

def commentsHashtag(lines):
    """
    :param lines: a list of lines from the source file
    :return: a dictionary with the #comments and the line where it is written
    """
    commentDico = {}
    for lineNumber in range(len(lines)):
        i = 0
        isComment = False
        comment = ''
        while i < len(lines[lineNumber]):

            if lines[lineNumber][i] == '#':
                isComment = True
            if isComment and lines[lineNumber][i] != '#':
                comment = comment + lines[lineNumber][i]
            i += 1
        if comment != '':
            commentDico['ligne ' +str(lineNumber)] = [comment, len(comment)]
    return commentDico

print(commentsHashtag(fichierLecture()))

def commentBlocks(lines):
    """
    :param lines: a list of lines from the source file
    :return: a dictionary in which all the block comments are ordered by is "=begin" line
    """
    commentDico = {}
    isBlock = False
    for lineNumber in range(len(lines)):
        if isBlock and lines[lineNumber][:4] != '=end':
            block += lines[lineNumber]
        if isBlock and lines[lineNumber][:4] == '=end':
            isBlock = False
            commentDico['ligne '+str(blockLine)] = [block, len(block)]
        if lines[lineNumber][:6] == '=begin':
            isBlock = True
            block = lines[lineNumber][6:]
            blockLine = lineNumber
            pass
    return commentDico

print(commentBlocks(fichierLecture()))

def commentCount(lines):
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
