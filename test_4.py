import pytest
@pytest.fixture
def numbers():
    a=10
    b=20
    c=25
    return [a,b,c]


def test_method1(numbers):
    x=15
    assert numbers[0]==x

def test_method2(numbers):
    y=20
    assert numbers[1]==y

def test_method3(numbers):
    z = 25
    assert numbers[2] == z

#fictures in pytest are used when we want to run some code before test
#@pytest.mark.xfail when you know that the code is going to fail 
#@pytest.mark.skip -when you want to skip any code