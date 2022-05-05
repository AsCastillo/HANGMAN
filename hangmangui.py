from tkinter import *
from tkinter import messagebox
import random
from words import word_list

h_picture = ['./assets/h7.png','./assets/h6.png','./assets/h5.png', './assets/h4.png','./assets/h3.png','./assets/h2.png','./assets/h1.png']

def get_word():
    word = random.choice(word_list)
    return word.upper()
    
class Hangman:
    def __init__(self, state):
        self.word = state
        print(self.word)
        self.word_completion = "_" * len(self.word)
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.tries = 6
    
    def set_word_completion(self, guess):
        word_as_list = list(self.word_completion)
        indices = [i for i, letter in enumerate(self.word) if letter == guess]
        for index in indices:
            word_as_list[index] = guess
        self.word_completion = "".join(word_as_list)
        if "_" not in self.word_completion:
            self.guessed = True
    
    def get_word_completion(self):
        word_completion = " ".join(self.word_completion)
        return word_completion
    
    def play(self, guess):
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                return "You already guessed the letter " + guess
            elif guess not in self.word:
                self.tries -= 1
                self.guessed_letters.append(guess)
                return "" + guess + " is not in the State."
            else:
                self.guessed_letters.append(guess)
                self.set_word_completion(guess)
                if self.guessed == True:
                    return "Congrats, you guessed the State! Maybe you should be President!"
                return "Good job, " + guess + " is in the State!"
        elif len(guess) >= len(self.word):
            if guess in self.guessed_words:
                return "You already guessed the State " + guess
            elif guess != self.word:
                self.tries -= 1
                self.guessed_words.append(guess)
                return "" + guess + " is not the State."
            else:
                self.guessed = True
                self.word_completion = self.word
                return "Congrats, you guessed the State! Maybe you should be President!"
        else:
            return ("Not a valid guess.")

class HangmanGUI:
    def __init__(self):
        
        self.hangman = Hangman(get_word())
        
        self.main_window = Tk()
        self.main_window.title('Hangman')
        
        # Frame
        self.top_frame = Frame(self.main_window)
        self.mid_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        self.result_frame = Frame(self.main_window)
        
        # Add hangman image
        
        self.image = PhotoImage(file=h_picture[self.hangman.tries])
        self.image_label = Label(self.top_frame, image=self.image)
        self.image_label.pack(side='left')
    
        self.word = StringVar()
        self.word.set(self.hangman.get_word_completion())
        self.word_label = Label(self.mid_frame, textvariable=self.word)
        self.word_label.pack(side='left')
        
        self.instruction_label = Label(self.bottom_frame, text="Please guess a letter or word:")
        self.instruction_label.pack(side='left')
        
        self.entry = Entry(self.bottom_frame)
        self.entry.pack(side='left')
        
        self.result = StringVar()
        self.result_label = Label(self.result_frame, textvariable=self.result)
        self.result_label.pack(side='left')
        
        self.button = Button(self.bottom_frame, text="Try", command=self.play)
        self.button.pack(side='left')
        
        
        
        # Pack Frame
        self.top_frame.pack(ipadx=20, ipady=20)
        self.mid_frame.pack(ipadx=20, ipady=20)
        self.bottom_frame.pack(ipadx=20, ipady=20)
        self.result_frame.pack(ipadx=20, ipady=20)
        
        mainloop()
        
        
    def play(self):
        guess = str(self.entry.get()).upper()
        self.entry.delete(0, len(guess))
        result = self.hangman.play(guess)
        
        self.word.set(self.hangman.get_word_completion())
        self.result.set(result)
        
        self.update_image()
        self.main_window.update()
        
        self.is_end()
    
    def update_image(self):
        self.image = PhotoImage(file=h_picture[self.hangman.tries])
        self.image_label.configure(image=self.image)
        self.image_label.image = self.image

    def is_end(self):
        if (self.hangman.guessed == True):
            res = messagebox.askyesno("WIN", "Congrats, you guessed the State! Maybe you should be President! Want to play again ?")
            if (res == True):
                self.hangman = Hangman(get_word())
                self.word.set(self.hangman.get_word_completion())
                self.result.set("")
                self.update_image()
                self.main_window.update()
            else:
                self.main_window.destroy()
        if (self.hangman.tries == 0):
            res = messagebox.askyesno("LOSE", "Sorry, you ran out of tries. The State was " + self.hangman.word + ". Maybe next time! Want to play again ?")
            if (res == True):
                self.hangman = Hangman()
                self.word.set(self.hangman.get_word_completion())
                self.result.set("")
                self.update_image()
                self.main_window.update()
            else:
                self.main_window.destroy()
    
if __name__ == "__main__":
    handman = HangmanGUI()