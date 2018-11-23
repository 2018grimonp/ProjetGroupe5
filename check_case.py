import math
"""
On considere que l'on a en entrée un tableau contenant tout les noms des variables contenues dans le code.
Ce tableau a été obtenu avec le programme test_variable.
On considère ici les conventions de nommage CamelCase et python.
On sépare d'abord les mots dans un nom de variable, puis on verifie que les mots existent (et que l'ensemble veut bien dire qqch)
"""


#Ouverture d'un dictionnaire de languie française.
l="liste.de.mots.francais.frgut.txt"
def readLines():  # retire les '/n' d'un fichier texte 
	L=[]
	with open(l,'r') as fp:
		for line in fp:
			line=line.replace('\n', '')
			L.append(line)
	return L


"""c'est deux programmes renvoi un tabelau contenant les different nom en minuscules des noms des variables"""


#Fonction qui renvoie True si la string contient des majuscules.
def il_y_a_maj(str):
	for char in str:
		if ord(char)>=65 and ord(char)<=90:
			return True
	return False

#Convertit maVariabble en ["ma","variable"]
def parse_camel_case(name):
	noms=[]
	if not il_y_a_maj(name):      #on test s'il y a des majuscules
		return [name]
	else:
		array=[]
		lastindex=0
		for i in range(len(name)):
			if ord(name[i])>=65 and ord(name[i])<=90:
				array.append(name[lastindex:i].lower())
				lastindex=i
		array.append(name[lastindex:len(name)].lower())
		return array 

#Convertit ma_variable en ["ma","variable"]
def parse_snake_case(str):  #str=le nom d'UNE variable
	return str.split("_")

#Détermine la convention de nommage (si elle est cohérente) et vérifie que les mots existent dans le dictionnaire
def NommageCoherent(list_str):	#on prend en argument la liste des noms des variables utiles 
	dictionnaire=readLines()
	snake_case_count=0
	camel_case_count=0
	both_case_count=0
	in_dictionnary=0
	not_in_dictionnary=0
	for name in list_str:
		if name.find("_")!=-1 and not il_y_a_maj(name):
			snake_case_count+=1		
			array=parse_snake_case(name)
			for word in array:
				if word in dictionnaire:
					in_dictionnary+=1
				else:
					not_in_dictionnary+=1
		elif il_y_a_maj(name):
			camel_case_count+=1
			array=parse_camel_case(name)
			for word in array:
				if word in dictionnaire:
					in_dictionnary+=1
				else:
					not_in_dictionnary+=1
				
		else:
			both_case_count+=1
			if name in dictionnaire:
				in_dictionnary+=1
			else:
				not_in_dictionnary+=1
	
	#print("Vous utilisez la convention de nommage camelCase à "+str(camel_case_count*100//(snake_case_count+camel_case_count))+"%.")
	#print("Vous utilisez la convention de nommage snake_case à "+str(snake_case_count*100//(snake_case_count+camel_case_count))+"%.")
	#print("Les mots que vous utilisez dans vos noms de variables existent à "+str(in_dictionnary*100//(in_dictionnary+not_in_dictionnary))+"% dans le dictionnaire.")
	pourcentagecc=(camel_case_count/(len(list_str)))
	pourcentagesc=(snake_case_count/(len(list_str)))
	pourcentagecc_=(camel_case_count/(camel_case_count+snake_case_count))
	pourcentagesc_=(snake_case_count/(camel_case_count+snake_case_count))
	return [pourcentagecc,pourcentagesc,pourcentagecc_,pourcentagesc_]

def returnmain(list_str):
	pourcentagecc,pourcentagesc,pourcentagecc_,pourcentagesc_=NommageCoherent(list_str)[0],NommageCoherent(list_str)[1],NommageCoherent(list_str)[2],NommageCoherent(list_str)[3]
	mix=1-((pourcentagecc)+(pourcentagesc))
	note=4*pourcentagecc_**2-4*pourcentagecc_+1							
	return ["Convention de Nommage-Analyse de la cohérence de la convention de nommage-camelCase+snake_case+Indéterminé-"+str(math.floor(pourcentagecc*100))+"+"+str(math.floor(pourcentagesc*100))+"-Note : "+str(round(note*10))+"/10-|",round(note*10)]

