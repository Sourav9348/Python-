from bank import value

def main():
    test_hello()
    test_hstart()
    test_other()
    test_number()


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("HeLlO") == 0

def test_hstart():
    assert value("hi") == 20
    assert value("Hay there") == 20

def test_other():
    assert value("What's up?") == 100
    assert value("give me now") == 100

def test_number():
    assert value("4") == 100

if __name__ == "__main__":
    main()
