from tools.pluralize import run

def test_pluralize():
    # Regular nouns
    assert run("cat") == "cats"
    assert run("dog") == "dogs"

    # Words ending in -s, -sh, -ch, -x, -z
    assert run("bus") == "buses"
    assert run("box") == "boxes"
    assert run("church") == "churches"

    # Words ending in -y preceded by a consonant
    assert run("city") == "cities"
    assert run("boy") == "boys"

    # Words ending in -f / -fe
    assert run("leaf") == "leaves"
    assert run("knife") == "knives"

    # Irregular / Uncountable / Generic nouns
    assert run("man") == "men"
    assert run("fish") == "fish"
    assert run("child") == "children"
    assert run("octopus") == "octopuses"

    # Error handling for empty or invalid inputs
    assert "Error" in run("")
    assert "Error" in run("   ")
    assert "Error" in run()