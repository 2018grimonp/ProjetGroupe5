import pytest
import appelvariable
from main import readLines

path="test_candidats/event_candidate_a_test.rb.rb"

def test_numlignevarglo():
    lines=readLines(path)
    result=appelvariable.numlignevarglo(lines)
    assert type(result) == list
    assert result[:68] == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,41,42,43,44,45,46,47,48,52,62,65,66,67,68,69,95,116,133,134,135,136,137,138,139,140,141,142,143,144,145,146]

def test_varglob():
    lines=readLines(path)
    result=appelvariable.varglob(lines)
    assert type(result) == list
    assert result[:1] == ["sel.table_name",2]

def test_varglobefore():
    lines=readLines(path)
    result_1=appelvariable.varglobefore(1,lines)
    assert type(result_1) == list
    assert result_1 == []

def test_textefonctions():
    lines=readLines(path)
    result=appelvariable.textefonctions(lines)
    assert type(result) == list
    assert result[:1] == ["KIND"]