from plates import is_valid

def main():
    test_character_size()
    test_start_with_two_letters()
    test_numbers_in_middle()
    test_number_zero()
    test_punctuation()


def test_character_size():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_start_with_two_letters():
    assert is_valid("AB") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False

def test_numbers_in_middle():
    assert is_valid("ABC123") == True
    assert is_valid("ABC12D") == False
    assert is_valid("ABC012") == False

def test_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3 14") == False
    assert is_valid("PI3?14") == False

if __name__ == "__main__":
    main()
