from main import greet

def test_greet():
    assert greet("Aswath") == "Hello, Aswath!"
    assert greet("World") == "Hello, World!"