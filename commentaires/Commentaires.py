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
            if isComment :
                comment = comment + lines[lineNumber][i]
            i += 1
        if comment != '':
            commentDico[lineNumber] = comment
    return commentDico

print(commentsHashtag(fichierLecture()))

def commentBlocks(lines):
    """
    :param lines: a list of lines from the source file
    :return: a dictionary in which all the block comments are ordered by is "=begin" line
    """
    commentDico = {}
    for lineNumber in range(len(lines)):
        words = TextBlob(lines[lineNumber])

