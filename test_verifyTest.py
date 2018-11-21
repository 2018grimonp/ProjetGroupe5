# ==== ==== ==== ====
#
#   test_verifyTest.py
#
#   Test pour verifyTest.py
#
#   Dernière modification : 21/11/2018
#
#	2018
#
# ==== ==== ==== ====

# TO DO : améliorer les tests

import pytest
import verfiyTest as toTest
from main import readLines

PATH = "test_candidats/event_candidate_a_test.rb.rb"

def test_rechercheEnd():
    lines = readLines(path)
    result_0 = rechercheEnd(lines, 3)
    assert type(result_0) == int    # rechercheEnd doit renvoyer un entier
    assert result_0 != -1           # rechercheEnd ne doit pas renvoyer une erreur
    assert result_0 == 6            # rechercheEnd(lines, 3) devrait normalement renvoyer 6 avec le fichier de tests utilisé

def test_isTest():
    lines = readLines(path)
    result_0 = isTest(lines)
    assert type(result_0) == bool   # isTest doit renvoyer un boolean
    assert result_0 != -1           # isTest ne doit pas renvoyer une erreur
    assert result_0 == True         # isTest(lines) devrait normalement renvoyer True avec le fichier de tests utlilisé

def test_countTests():
    lines = readLines(path)
    result_0 = countTests(lines)
    assert type(result_0) == tuple      # countTests doit renvoyer un tuple
    assert result_0 != -1               # countTests ne doit pas renvoyer une erreur
    assert type(result_0[0]) == int     # la 1ere partie du tuple renvoyé par countTests doit être un int
    assert type(result_1[1]) == dict    # la 2nds partie du tuple renvoyé par countTests doit être un dict

def test_printStatsTests():
    lines = readLines(path)
    result_0 = printStatsTests(lines)
    assert type(result_0) == None   # printStatsTests ne doit rien renvoyer
