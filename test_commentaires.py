import commentaires as c
import pytest

lines = ['Une ligne qui sert à rien', '#Un commentaire normal', 'une ligne inutile #avec un com à la fin', '=begin un commentaire en block', 'ca continue', '=end']
try:
        fichier = open('./liste.de.mots.francais.frgut.txt', 'r')
        mots = [mot.replace('\n', '') for mot in fichier.readlines()]
        motsDecode = mots
except IOError:
    print('aille')

def test():
    assert c.commentsHashtag(lines) == {(1,): [['Un commentaire normal'], 1], (2,): [['avec un com à la fin'], 1]}
    assert c.commentBlocks(lines) == {(3, 4): [[' un commentaire en block', 'ca continue'], 35]}
    assert c.commentCount(lines) == (3, {(1,): [['Un commentaire normal'], 1], (2,): [['avec un com à la fin'], 1], (3, 4): [[' un commentaire en block', 'ca continue'], 35]})
    assert c.detectCom(lines[0]) == 0
    assert c.detectCom(lines[1]) == 1
    assert c.detectCom(lines[2]) == 19
    assert c.detectCom(lines[3]) == -1
    assert c.detectCom(lines[4]) == 0
    assert c.detectCom(lines[5]) == -2
    assert c.retirerCom(lines) == ['Une ligne qui sert à rien', '', 'une ligne inutile ']
    assert c.analyseCom(lines) == ([0, 21, 20, 24, 11, 0], 0.2824427480916031, 0.6666666666666666, 3)
    assert c.howCommented(lines) == (True, (12.666666666666666, 9.792287214378922), (0.6666666666666666, 0.2824427480916031))
    assert c.commentsWords(lines) == ({'un': 3, 'commentaire': 2}, ['normalavec', 'com', 'à', 'la', 'fin', 'en', 'blockca', 'continue'])
    assert c.isFrancais('bonjour', motsDecode)
    assert not c.isFrancais('aoriezur', motsDecode)
    assert c.ratioFrancais(lines) == (1.0, 0.625)


