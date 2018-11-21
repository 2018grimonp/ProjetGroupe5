import pytest
import trouve_fonction
import main


testFonction1=main.readLines("C:\Users\Tim\PycharmProjects\ProjetGroupe5\test_candidats\event_candidate_a.rb.rb.rb")
testFonction2=main.readLines("C:\Users\Tim\PycharmProjects\ProjetGroupe5\test_candidats\event_candidate_a_test.rb.rb")
testFonction3=["akmdf","def rpsafk","def","end"]


def testCountFonction():
    assert trouve_fonction.count_fonction(testFonction1)==[1,1,7,3,3,5,4,4,4,10]
    assert trouve_fonction.count_fonction(testFonction2)==[]
    assert trouve_fonction.count_fonction(testFonction3)[:6]=="Erreur"
