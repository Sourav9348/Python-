from working import convert
import pytest

def main():
    test_wrong_format()
    test_time()
    test_wrong_hour()
    test_wrong_minute()


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12:00 AM to 8:50 PM") == "00:00 to 20:50"


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM - 5:60 PM")

if __name__ == "__main__":
    main()
