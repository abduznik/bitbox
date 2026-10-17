from tools.pluralize import run

def test_pluralize():
    
    assert run("cat") == "cats"
    assert run("dog") == "dogs"

    assert run("bus") == "buses"
    assert run("box") == "boxes"
    assert run("church") == "churches"

    assert run("city") == "cities"
    assert run("boy") == "boys"

    assert run("leaf") == "leaves"
    assert run("knife") == "knives"

    assert run("man") == "men"
    assert run("fish") == "fish"
    assert run("child") == "children"

    assert "Error" in run()