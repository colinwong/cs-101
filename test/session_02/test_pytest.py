from session_02 import inc_dec

def test_increment():
  assert inc_dec.increment(3) == 4

def test_decrement():
  assert inc_dec.decrement(4) == 3