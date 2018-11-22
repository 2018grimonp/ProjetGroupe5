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
import checkIndentation as toTest

def test_retirerIndentation():
    assert toTest.retirerIndentation(["    mot"]) == ["mot"]
    assert toTest.retirerIndentation(["mot"]) == ["mot"]
    assert toTest.retirerIndentation(["mot    "]) == ["mot    "]

def test_printIndentation():
    assert toTest.printIndentation(["mot1", "mot2"], True) == -1
    assert toTest.printIndentation(["      mot1", "   mot2"], True) == 3
    assert toTest.printIndentation(["    mot1"], True) == 4
