
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
    
def test_get_word_completion():
    hangman = Hangman("OHIO")
    assert hangman.get_word_completion() == "_ _ _ _"

def test_play_guess_letter():
    hangman = Hangman("OHIO")
    result = hangman.play("O")
    assert result == "Good job, O is in the State!"

def test_play_already_guess_letter():
    hangman = Hangman("OHIO")
    hangman.play("O")
    result = hangman.play("O")
    assert result == "You already guessed the letter O"

def test_play_guess_state():
    hangman = Hangman("OHIO")
    result = hangman.play("OHIO")
    assert result == "Congrats, you guessed the State! Maybe you should be President!"

def test_play_guess_not_good_state():
    hangman = Hangman("OHIO")
    result = hangman.play("ALABAMA")
    assert result == "ALABAMA is not the State."
    
def test_play_guess_already_not_good_state():
    hangman = Hangman("OHIO")
    hangman.play("ALABAMA")
    result = hangman.play("ALABAMA")
    assert result == "You already guessed the State ALABAMA"