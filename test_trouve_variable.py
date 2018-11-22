import pytest
import trouve_variables as toTest

def readLines(l):  # retire les '/n' d'un fichier texte 
    L=[]
    fp=open(l,'r')
    lines=fp.readlines()
    for line in lines:
        line=line.replace('\n', '')
        L.append(line)
    return L

PATH="test.rb"

def test_countVariables():
    lines = readLines(PATH)
    result=toTest.countVariables(lines)
    assert type(result) == list
    assert "KIND" in result

def test_snailVariables():
    lines = readLines(PATH)
    result=toTest.snailVariables(lines, ["KIND"])
    assert type(resul) == list
    assert ["KIND"] + result == lines
