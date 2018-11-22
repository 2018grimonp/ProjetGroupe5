import pytest
import trouve_fonction
import commentaires
import checkIndentation


def readLines(l):  # retire les '/n' d'un fichier texte
    L=[]
    fp=open(l,'r')
    lines=fp.readlines()
    for line in lines:
        line=line.replace('\n', '')
        L.append(line)
    return L

testFonction1=readLines("event_candidate_a.rb.rb")
testFonction2=readLines("event_candidate_a_test.rb.rb")
testFonction3=["akmdf","  def rpsafk","def u","end"]

testFonction1=checkIndentation.retirerIndentation(commentaires.retirerCom(testFonction1))
testFonction2=checkIndentation.retirerIndentation(commentaires.retirerCom(testFonction2))
testFonction3=checkIndentation.retirerIndentation(commentaires.retirerCom(testFonction3))

b=trouve_fonction.printFonction(testFonction2)
b=trouve_fonction.printFonction(testFonction3)
b=trouve_fonction.printFonction(testFonction1)

