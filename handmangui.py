import tkinter
import tkinter.messagebox
import random
from words import word_list


class HandmanGUI:
    def __init__(self):
        self.word = self.get_word()
        self.word_completion = "_" * len(self.word)
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.tries = 6
        
        self.main_window = tkinter.Tk()
        self.main_window.title('Hangman')
        
        self.instruction_label_var = tkinter.StringVar()
        self.instruction_label_var.set("Please guess a letter or word:")
        self.instruction_label = tkinter.Label(self.main_window, textvariable=self.instruction_label_var)
        
        self.instruction_label.pack(side='left')
        
        
        self.display_hangman()
        
        
        self.word_label_var = tkinter.StringVar()
        self.word_label_var.set(self.word_completion)
        self.word_label = tkinter.Label(self.main_window, textvariable=self.word_label_var)
        
        self.word_label.pack(side='left')
        
        
        self.r_label_var = tkinter.StringVar()
        self.r_label = tkinter.Label(self.main_window, textvariable=self.r_label_var)
        
        self.r_label.pack(side='left')
        
        
        self.input = tkinter.StringVar()
        self.entry = tkinter.Entry(self.main_window)
        self.entry.pack(side='left')
        
        self.button = tkinter.Button(self.main_window, text="Try", command=self.getGuess())
        self.button.pack(side='left')
        
        
        
        
        tkinter.mainloop()
        
        
    def get_word(self):
        word = random.choice(word_list)
        return word.upper()
    
    def display_hangman(self):
        if self.tries == 1 :
            print("one tries")
            
    def getGuess(self):
        guess = str(self.entry.get())
        print(guess)
        if len(guess) == 1 and guess.isalpha():
            print("bonjour")
            # if guess in self.guessed_letters:
            #     self.r_label_var.set("You already guessed the letter", guess)
            #     print(self.r_label_var)
            # elif guess not in self.word:
            #     self.r_label_var.set(guess, "is not in the State.")
            #     print(self.r_label_var)
            #     self.tries -= 1
            #     self.guessed_letters.append(guess)
            # else:
            #     self.r_label_var.set("Good job,", guess, "is in the State!")
            #     print(self.r_label_var)
            #     self.guessed_letters.append(guess)
            #     word_as_list = list(self.word_completion)
            #     indices = [i for i, letter in enumerate(self.word) if letter == guess]
            #     for index in indices:
            #         word_as_list[index] = guess
            #     self.word_completion = "".join(word_as_list)
            #     if "_" not in self.word_completion:
            #         self.guessed = True
            #     elif len(guess) == len(self.word) and guess.isalpha():
            #         if guess in self.guessed_words:
            #             self.r_label_var.set("You already guessed the State", guess)
            #             print(self.r_label_var)
            #         elif guess != self.word:
            #             self.r_label_var.set(guess, "is not the State.")
            #             print(self.r_label_var)
            #             self.tries -= 1
            #             self.guessed_words.append(guess)
            #         else:
            #             self.guessed = True
            #             self.word_completion = self.word
            #     else:
            #         self.r_label_var.set("Not a valid guess.")
            #         print(self.r_label_var)
            #     # print(display_hangman(tries))
            #     self.word_label_var.set(self.word_completion)
        self.r_label.pack(side='left')
        self.word_label.pack(side='left')



if __name__ == "__main__":
    handman = HandmanGUI()