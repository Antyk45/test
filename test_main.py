import os

JOE = os.environ["joe"] 

def test_1():
  print(os.environ["joe"])
  print(JOE)
  
  if JOE == "Biden":
    assert 2 == 2
    
  else:
    assert 2 == 3
