
from hangmangui import Hangman, get_word
from words import word_list

def test_get_word():
    hangman = Hangman(get_word())
    for state in word_list:
        if (state == hangman.word):
            assert hangman.word == state

def test_set_word_completion():
    hangman = Hangman("OHIO")
    hangman.set_word_completion('O')
    assert hangman.word_completion == "O__O"
    
# def get_word_completion():
    
# def play():
    
