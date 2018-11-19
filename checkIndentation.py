

def retirerIndentation(lines):
	"""
	Retire les espaces devant les lignes
	:param lines: Liste des lignes du fichier
	""" 
	for i in range(len(lines)): 
		nbSpaces=0
		line=lines[i]
		for char in line:
			if char==" ":
				nbSpaces+=1
			else:
				break;
		lines[i]=lines[i][nbSpaces:]

		
	return lines


def printIndentation(lines):
	"""
	Vérifie l'indentation
	:param arraySpacesCount: Liste des nombres d'espaces devant chaque ligne
	"""
	
	#Compte le nombre d'espaces devant chaque ligne
	arraySpacesCount=[]
	for i in range(len(lines)):
		nbSpaces=0
		line=lines[i]
		for char in line:
			if char==" ":
				nbSpaces+=1
			else:
				break;
		arraySpacesCount.append(nbSpaces)

	#Détermine le nombre d'espaces correspondant l'indentation
	indentLength=255
	for count in arraySpacesCount:
		if count < indentLength and count!=0:
			indentLength=count
	print("L'identation semble être de "+str(indentLength)+" espace(s).")

	#Vérifie que le nombre d'espaces devant chaque ligne est un multiple de l'indentation
	arrayIndentsCount=[]
	for i in range(len(arraySpacesCount)):
		count=arraySpacesCount[i]
		if count%indentLength!=0:
			print("Problème d'indentation ligne "+str(i)+ ". Le nombre d'espace n'est pas un multiple de l'indentation.")
		arrayIndentsCount.append(count//indentLength)

	#Vérifie qu'aucune ligne n'est indentée plusieurs fois par rapport à la précédente 	
	countOldLine=0
	for i in range(len(arrayIndentsCount)):
		countNewLine=arrayIndentsCount[i]
		if abs(countNewLine-countOldLine)>1:
			print("Problème d'indentation ligne "+str(i)+ ". Indentation supplémentaire inatendue.")
		countOldLine=countNewLine	

	

