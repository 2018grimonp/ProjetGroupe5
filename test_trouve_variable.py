import pytest
import trouve_variable 
from main import readLines

PATH="test_candidats/event_candidate_a_test.rb.rb"

def test_countVariables():
    lines = readLines(PATH)
    result=test_variable.countVariables(lines)
    assert type(result) == list
    assert" KIND" in result

    
