from um import count

def test_um():
    assert count("um, um, um")==3
    assert count("um, yummy")==1
    assert count("um...UM")==2
    assert count("My name is abrar, Um i am Um")==2
def test_zero():
    assert count("yummy")==0
    assert count("hello muma")==0
