import duplicationFonction

CodeTest1=["af","  fs","george = 1","def skad(george)","babar","george = 1","split #françois","end","b","def j","d if do","end","end"]
CodeTest2=["def","salut","end"]
CodeControle1=["af","bob = 1","  fs","def skad(bob)","babar","bob = 1","split #frank","end","a","def sfs","d if don","end","end"]
CodeControle2=["sporz","salutt","salut"]


def test_controle_duplication():
    assert duplicationFonction.controle_duplication(CodeTest2,80,CodeControle2)==[[{'pourcentage': 83.33333333333334, 'ligneControle': 1}, {'pourcentage': 100.0, 'ligneControle': 2}]]
    assert duplicationFonction.controle_duplication(CodeTest1,80,CodeControle1)==[[{'pourcentage': 100.0, 'ligneControle': 4}], [{'pourcentage': 93.75, 'ligneControle': 10}]]
    assert duplicationFonction.controle_duplication(CodeTest1,80,CodeControle2)==[[],[]]
