"""

Program: GUI_template.py
Author: Matthew 7/10/2023

A GUI-based application of a number guessing game

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly,


"""

from breezypythongui import EasyFrame
import random
# Other imports go here

# Class header
class GuessingGame(EasyFrame):
	# Definition of our class constructor
	def __init__(self):
		EasyFrame.__init__(self, title="Guessing Game", width=260, height=180)

	#Initialize the instance variables for the class
		self.magicNumber = random.randint(1, 10)
		self.count = 0
		self.hintLabel = self.addLabel(text="Guess a Number between 1 and 100", row=0, column=0, columnspan=2)
		self.addLabel(text="Your guess:", row=1, column=0)
		self.guessField = self.addIntegerField(value=0, row=1, column=1)
		self.nextButton = self.addButton(text="Next", row=2, column=0, command=self.nextGuess)
		self.newButton = self.addButton(text="New Game", row=2, column=1, command=self.newGame)

	def nextGuess(self):
		self.count += 1
		guess = self.guessField.getNumber()
		# Logic that determines the game's outcome
		if guess == self.magicNumber:
			self.hintLabel["text"] = "You've guessed it in " + str(self.count) + " tries"
			self.nextButton["state"] = "disabled"
		elif guess < self.magicNumber:
			self.hintLabel["text"] = "Sorry, your guess was too small"
		else:
			self.hintLabel["text"] = "Sorry, your guess was too high"
	def newGame(self):
		"""Resets the data and GUI to their original states."""
		self.magicNumber = random.randint(1, 10)
		self.count = 0
		self.hintLabel["text"] = "Guess a Number between 1 and 100"
		self.guessField.setNumber(0)
		self.nextButton["state"] = "normal"


		
# Global definition of the main() method
def main():
	GuessingGame().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()