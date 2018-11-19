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
    :return: a dictionary with the comment and the line where it is written
    """
    commentList = {}
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
            commentList[lineNumber] = comment
    return commentList

print(commentsHashtag(fichierLecture()))
