from tools.symmetric_difference import run

def test_symmetric_difference():
  
    assert run("1,2", "2,3") == "1,3"
    
    assert run("1,2", "3,4") == "1,2,3,4"
    
    assert run("1,2", "1,2") == ""
    
    assert "Error" in run("1,2")