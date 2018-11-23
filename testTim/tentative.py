import pytest
import trouve_fonction
import commentaires
import checkIndentation

"""
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
"""
import duplicationFonction

CodeTest1=["af","  fs","george = 1","def skad(george)","babar","george = 1","split #françois","end","b","def j","d if do","end","end"]
CodeTest2=["def","salut","end"]
CodeControle1=["af","bob = 1","  fs","def skad(bob)","babar","bob = 1","split #frank","end","a","def sfs","d if don","end","end"]
CodeControle2=["sporz","salutt","salut"]



print(duplicationFonction.controle_duplication(CodeTest2,80,CodeControle2))
print(duplicationFonction.controle_duplication(CodeTest1,80,CodeControle1))
