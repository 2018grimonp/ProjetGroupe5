import pytest
import trouve_fonction
import main

def readLines(l):  # retire les '/n' d'un fichier texte
    L=[]
    fp=open(l,'r')
    lines=fp.readlines()
    for line in lines:
        line=line.replace('\n', '')
        L.append(line)
    return L

testFonction1=main.readLines("event_candidate_a.rb.rb.rb")
testFonction2=main.readLines("test.rb")
testFonction3=["akmdf","def rpsafk","def","end"]


def testCountFonction():
    assert trouve_fonction.count_fonction(testFonction1)==[1,1,7,3,3,5,4,4,4,10]
    assert trouve_fonction.count_fonction(testFonction2)==[]
    assert trouve_fonction.count_fonction(testFonction3)[:6]=="Erreur"
