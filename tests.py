import spaceman
import random
import io
import sys
import unittest

#UNIT TESTS
class TestStringMethods(unittest.TestCase):
    def tests_is_word_guessed(selfself):

        assert spaceman.is_word_guessed("a", {"a"}) == True
        assert spaceman.is_word_guessed("a", {"b"}) == False

    def tests_is_guess_in_word(self):
        assert spaceman.is_guess_in_word("a", "a") == True

    def test_get_guess(self):
        assert spaceman.get_guess() != None

    def test_load_word(self):
        assert spaceman.load_word() != None

    def test_spaceman(self):
        assert spaceman.spaceman("") == None

if __name__ == '__main__':
    unittest.main()
#
# if __name__ == "__main__":
#     # Run the test function
#     tests_is_word_guessed()
#     tests_is_guess_in_word()
#     test_get_guess()
#     test_load_word()
#     test_spaceman()
