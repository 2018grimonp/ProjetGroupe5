import pytest
import appelvariable
from commentaires import retirerCom
from checkIndentation import retirerIndentation

def readLines(l):  # retire les '/n' d'un fichier texte 
    L=[]
    fp=open(l,'r')
    lines=fp.readlines()
    for line in lines:
        line=line.replace('\n', '')
        L.append(line)
    return L

path="test.rb"

def test_numlignevarglo():
    lines=readLines(path)
    lines=retirerCom(lines)
    lines=retirerIndentation(lines)
    result=appelvariable.numlignevarglo(lines)
    assert type(result) == list
    for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]:
        assert i in result
    for i in [38,39,40]:
        assert not i in result

def test_varglobal():
    lines=readLines(path)
    lines=retirerCom(lines)
    lines=retirerIndentation(lines)
    result=appelvariable.varglobal(lines)
    assert type(result) == list
    assert result[0] == ["self.table_name",2]

def test_varglobefore():
    lines=readLines(path)
    lines=retirerCom(lines)
    lines=retirerIndentation(lines)
    result_1=appelvariable.varglobefore(1,lines)
    assert type(result_1) == list
    assert result_1 == []

def test_textefonctions():  #seul qui marche......
    lines=readLines(path)
    lines=retirerCom(lines)
    lines=retirerIndentation(lines)
    result=appelvariable.textefonctions(lines)
    assert type(result) == list
    assert result[0][0] == 38  #la premiere fonction commence ligne 38

def test_appelvar():
    lines=readLines(path)
    lines=retirerCom(lines)
    lines=retirerIndentation(lines)
    result=appelvariable.appelvar(lines)
    assert type(result)== int
    assert result != 0
