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
    result=appelvariable.numlignevarglo(lines)
    assert type(result) == list
    assert result[:2] == [1,2]
def test_varglob():
    lines=readLines(path)
    result=appelvariable.varglob(lines)
    assert type(result) == list
    assert result[:1] == ["self.table_name",2]

def test_varglobefore():
    lines=readLines(path)
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
    result=appelvariable.appelvar(lines)
    assert type(result)== int
    assert result != 0
