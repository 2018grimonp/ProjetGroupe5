from Main import *

"""l='Bonjour, comment vas-tu? \n Cet exo est top! \n Merci beaucoup! \n'

def test_readLines():
    L=readLines(l)
    assert '\n' not in L  --> pb avec le input()"""

lines=readLines(event_candidate_a_test)

print(lines)

def test_nbassert():
    (t,a)=nbassert(l)
    assert t<=a
    assert t>=1





