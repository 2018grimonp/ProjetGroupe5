


def extractIndentation(lines):
	
	for line in lines:
		nbSpaces=0
		for char in line:
			if char=" ":
				nbSpace+=1
