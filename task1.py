import tkinter as tk
import random

# List of words for the Hangman game
words = ["python", "java", "kotlin", "javascript", "hangman", "programming", "development"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.config(bg="#F0F0F0")

        self.word = random.choice(words).upper()
        self.guessed = ["_"] * len(self.word)
        self.attempts = 6
        self.guessed_letters = []

        self.setup_ui()

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="#FFFFFF")
        self.canvas.pack(pady=20)

        self.label = tk.Label(self.root, text=" ".join(self.guessed), font=("Helvetica", 20), bg="#F0F0F0")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Helvetica", 20))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_guess)

        self.message = tk.Label(self.root, text=f"Attempts left: {self.attempts}", font=("Helvetica", 16), bg="#F0F0F0")
        self.message.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game, font=("Helvetica", 16), bg="#007BFF", fg="#FFFFFF")
        self.reset_button.pack(pady=10)

        self.draw_hangman()

    def check_guess(self, event):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.message.config(text="Invalid input. Enter a single letter.", fg="red")
            return

        if guess in self.guessed_letters:
            self.message.config(text="You already guessed that letter.", fg="red")
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed[idx] = guess
            self.label.config(text=" ".join(self.guessed))
        else:
            self.attempts -= 1

        self.message.config(text=f"Attempts left: {self.attempts}", fg="black")

        if "_" not in self.guessed:
            self.message.config(text="Congratulations! You've won!", fg="green")
            self.entry.config(state="disabled")
        elif self.attempts == 0:
            self.message.config(text=f"You've lost! The word was {self.word}", fg="red")
            self.entry.config(state="disabled")

        self.draw_hangman()

    def reset_game(self):
        self.word = random.choice(words).upper()
        self.guessed = ["_"] * len(self.word)
        self.attempts = 6
        self.guessed_letters = []

        self.label.config(text=" ".join(self.guessed))
        self.message.config(text=f"Attempts left: {self.attempts}", fg="black")
        self.entry.config(state="normal")

        self.draw_hangman()

    def draw_hangman(self):
        self.canvas.delete("all")
        if self.attempts <= 5:
            self.canvas.create_line(50, 250, 150, 250, width=2)
        if self.attempts <= 4:
            self.canvas.create_line(100, 250, 100, 50, width=2)
        if self.attempts <= 3:
            self.canvas.create_line(100, 50, 200, 50, width=2)
        if self.attempts <= 2:
            self.canvas.create_line(200, 50, 200, 100, width=2)
        if self.attempts <= 1:
            self.canvas.create_oval(180, 100, 220, 140, width=2)
        if self.attempts == 0:
            self.canvas.create_line(200, 140, 200, 200, width=2)
            self.canvas.create_line(200, 160, 170, 190, width=2)
            self.canvas.create_line(200, 160, 230, 190, width=2)
            self.canvas.create_line(200, 200, 170, 230, width=2)
            self.canvas.create_line(200, 200, 230, 230, width=2)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


