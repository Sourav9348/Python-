from um import count
import pytest

def main():
    test_1()
    test_2()
    test_3()
    test_4()


def test_1():
    assert count("Um, thanks for the album.") == 1


def test_2():
    assert count("um") == 1


def test_3():
   assert count("Um, thanks, um...") == 2

def test_4():
    assert count("Um?") == 1

if __name__ == "__main__":
    main()
