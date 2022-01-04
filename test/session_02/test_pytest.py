'''
Session 2 test.
'''
from session_02 import inc_dec


def test_increment():
    '''Test increment input'''
    assert inc_dec.increment(3) == 4


def test_decrement():
    '''Test decrement input'''
    assert inc_dec.decrement(4) == 3
