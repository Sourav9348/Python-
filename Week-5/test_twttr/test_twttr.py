from twttr import shorten

def main():
    test_cases()
    test_numbers()
    test_punctuation()


def test_cases():
    assert shorten("sourav") == "srv"
    assert shorten("SOURAV") == "SRV"
    assert shorten("SoUrAv") == "Srv"

def test_numbers():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("I'm Sourav. Who are You?") == "'m Srv. Wh r Y?"

if __name__ == "__main__":
    main()
