from tkinter import *
import random
from words import word_list

class Hangman:
    def __init__(self):
        self.word = self.get_word()
        print(self.word)
        self.word_completion = "_" * len(self.word)
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.tries = 6

    def get_word(self):
        word = random.choice(word_list)
        return word.upper()
    
    def set_word_completion(self, guess):
        word_as_list = list(self.word_completion)
        indices = [i for i, letter in enumerate(self.word) if letter == guess]
        for index in indices:
            word_as_list[index] = guess
        self.word_completion = "".join(word_as_list)
        if "_" not in self.word_completion:
            self.guessed = True
    
    def play(self, guess):
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                return ("You already guessed the letter", guess)
            elif guess not in self.word:
                self.tries -= 1
                self.guessed_letters.append(guess)
                return (guess, "is not in the State.")
            else:
                self.guessed_letters.append(guess)
                self.set_word_completion(guess)
                return "Good job, " + guess + " is in the State!"
        elif len(guess) == len(self.word) and guess.isalpha():
            if guess in self.guessed_words:
                return ("You already guessed the State", guess)
            elif guess != self.word:
                self.tries -= 1
                self.guessed_words.append(guess)
                return (guess, "is not the State.")
            else:
                self.guessed = True
                self.word_completion = self.word
                return ("Congrats, you guessed the State! Maybe you should be President!")
        else:
            return ("Not a valid guess.")

class HangmanGUI:
    def __init__(self):
        self.hangman = Hangman()
        
        self.main_window = Tk()
        self.main_window.title('Handman')
        
        # Frame
        self.top_frame = Frame(self.main_window)
        self.mid_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        self.instruction_label = Label(self.mid_frame, text="Please guess a letter or word:")
        self.instruction_label.pack(side='left')
        
        self.entry = Entry(self.mid_frame)
        self.entry.pack(side='left')
        
        self.word = StringVar()
        self.word.set(self.hangman.word_completion)
        self.word_label = Label(self.mid_frame, textvariable=self.word)
        self.word_label.pack(side='left')
        
        self.result = StringVar()
        self.result_label = Label(self.bottom_frame, textvariable=self.result)
        self.result_label.pack(side='left')
        
        self.button = Button(self.mid_frame, text="Try", command=self.play)
        self.button.pack(side='left')
        
        
        
        # Pack Frame
        self.top_frame.pack(ipadx=20, ipady=20)
        self.mid_frame.pack(ipadx=20, ipady=20)
        self.bottom_frame.pack(ipadx=20, ipady=20)
        
        mainloop()
        
        
    def play(self):
        guess = str(self.entry.get())
        result = self.hangman.play(guess)
        
        self.word.set(self.hangman.word_completion)
        self.result.set(result)
    
if __name__ == "__main__":
    handman = HangmanGUI()