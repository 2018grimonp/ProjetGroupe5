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


def testCountFonction():
    assert trouve_fonction.count_fonction(testFonction1)==[{'start': 31, 'longueur': 1, 'nom': 'opening?', 'end': 33}, {'start': 35, 'longueur': 1, 'nom': 'appointment?', 'end': 37}, {'start': 39, 'longueur': 7, 'nom': 'self.availabilities', 'end': 47}, {'start': 50, 'longueur': 3, 'nom': 'starts_at_cannot_be_greater_than_ends_at', 'end': 54}, {'start': 56, 'longueur': 3, 'nom': 'ends_at_cannot_be_a_different_day_than_starts_at', 'end': 60}, {'start': 62, 'longueur': 5, 'nom': 'hours_must_be_a_multiple_of_thirty_minutes', 'end': 68}, {'start': 70, 'longueur': 4, 'nom': 'same_kind_of_event_cannot_be_in_a_same_time_slot', 'end': 75}, {'start': 77, 'longueur': 4, 'nom': 'appointment_cannot_be_outside_of_opening_hours', 'end': 82}, {'start': 84, 'longueur': 4, 'nom': 'self.slots_available', 'end': 89}, {'start': 91, 'longueur': 9, 'nom': 'self.split_into_slots', 'end': 101}]
    assert trouve_fonction.count_fonction(testFonction2)==[]
    assert trouve_fonction.count_fonction(testFonction3)[:6]=="Erreur"



