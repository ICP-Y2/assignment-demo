from hello import greet_person

def test_greet_person(capsys):
    greet_person("Alice")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"

def test_greet_person_2(capsys):
    greet_person(123)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Numbers not allowed!"
    
def test_greet_person_3(capsys):
    greet_person("Smith John")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Smith John!"