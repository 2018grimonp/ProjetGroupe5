import commentaires as c

lines = ['Une ligne qui sert à rien', '#Un commentaire normal', 'une ligne inutile #avec un com à la fin', '=begin un commentaire en block', 'ca continue', '=end']

def test():
    assert c.commentsHashtag(lines) == {1: ['Un commentaire normal', 21], 2: ['avec un com à la fin', 20]}
    assert c.commentBlocks(lines) == {3: [' un commentaire en blockca continue', 35]}
    assert c.commentCount(lines) == (3, {1: ['Un commentaire normal', 21], 2: ['avec un com à la fin', 20], 3: [' un commentaire en blockca continue', 35]})
    assert c.detectCom(lines[0]) == 0
    assert c.detectCom(lines[1]) == 1
    assert c.detectCom(lines[2]) == 19
    assert c.detectCom(lines[3]) == -1
    assert c.detectCom(lines[4]) == 0
    assert c.detectCom(lines[5]) == -2
    assert c.retirerCom(lines) == ['Une ligne qui sert à rien', '', 'une ligne inutile ']
    assert c.analyseCom(lines) == ([0, 21, 20, 35, 0, 0], 0.5801526717557252, 0.5, 3)


