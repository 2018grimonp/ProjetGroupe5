

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


def printIndentation(lines, onTest = False):
	"""
	Vérifie l'indentation et renvoie une string qui représente un graphique
	:param arraySpacesCount: Liste des nombres d'espaces devant chaque ligne
	"""

	thereIsAproblem=False
	note=10
	
	#Compte le nombre d'espaces devant chaque ligne
	arraySpacesCount=[]
	for i in range(len(lines)):
		nbSpaces=0
		line=lines[i]
		estVide=True
		for char in line:
			if char==" ":
				nbSpaces+=1
			else:
				estVide=False
				break
		if not estVide:
			arraySpacesCount.append(nbSpaces)
			if(nbSpaces==1):
				print("truc " + str(i))
		else:
			arraySpacesCount.append(-1)

	#Détermine le nombre d'espaces correspondant l'indentation
	indentLength=255
	for count in arraySpacesCount:
		if count < indentLength and count!=0 and count!=-1:
			indentLength=count

	if indentLength!=255:
		print("L'identation semble être de "+str(indentLength)+" espace(s).")
		if onTest == True:
			return indentLength
	else:
		print("L'indentation ne peut être déterminée.")
		if onTest == True:
			return -1
		thereIsAproblem=True

	#Vérifie que le nombre d'espaces devant chaque ligne est un multiple de l'indentation
	arrayIndentsCount=[]
	count1=0
	problems=[]
	for i in range(len(arraySpacesCount)):
		count=arraySpacesCount[i]
		if count!=-1 and count%indentLength!=0:
			print("Problème d'indentation ligne "+str(i)+ ". Le nombre d'espace n'est pas un multiple de l'indentation.")
			problems.append(i)
			count1+=1
			note-=0.5
			thereIsAproblem=True
		arrayIndentsCount.append(count//indentLength)

	#Vérifie qu'aucune ligne n'est indentée plusieurs fois par rapport à la précédente 	
	countOldLine=0
	count2=0
	for i in range(len(arrayIndentsCount)):
		countNewLine=arrayIndentsCount[i]
		if countNewLine==-1 :
			continue
		if abs(countNewLine-countOldLine)>1 and not i in problems:
			print("Problème d'indentation ligne "+str(i)+ ". Indentation supplémentaire ou manquante inatendue.")
			count2+=1
			note-=0.25
			thereIsAproblem=True
		countOldLine=countNewLine	
	
	if not thereIsAproblem:
		print("Aucun problème d'indentation détecté.")
	
	return "Indentation 1/2-Proportion des erreurs d'indentation-Indentations inattendues+Indentations inconsistentes+Lignes bien indentées - "+str(count1*100//len(lines))+"+"+str(count2*100//len(lines))+"--|Indentation 2/2-Évaluation de l'indentation-Points+-"+str(note*10)+"- Note : "+str(int(note))+"/10 -|",int(note)
