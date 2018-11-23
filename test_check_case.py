# ==== ==== ==== ====
#
#   test_verifyTest.py
#
#   Test pour verifyTest.py
#
#   Dernière modification : 22/11/2018
#
#	2018
#
# ==== ==== ==== ====

import pytest
import check_case as toTest

def test_il_y_a_maj():
    assert toTest.il_y_a_maj("A") == True
    assert toTest.il_y_a_maj("a") == False

def test_parse_camel_case():
    assert toTest.parse_camel_case("aB") == ["a", "b"]

def test_parse_snake_case():
    assert toTest.parse_snake_case("a_b") == ["a", "b"]

def test_NommageCoherent():
    assert toTest.NommageCoherent(["unMot"]) == ["100", "0"]
