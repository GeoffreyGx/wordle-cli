import random
import words

class Letter:
    def __init__(self, letter):
        self.letter = letter

    def __str__(self):
        return self.letter
    
    def setState(self, state):
        self.state = state
    
class Word:
    def __init__(self, word):
        self.letters = []
        for letter in word:
            self.letters.append(Letter(letter))

    def __str__(self):
        return ''.join([str(letter) for letter in self.letters])
    
    def getRandomWord(self):
        return words.wordlist[random.randint(0, len(words.wordlist) - 1)]