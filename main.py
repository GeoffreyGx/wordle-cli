import random
import restart
import words

class Wordle:
    """
    Wordle game class. Utilisé pour jouer et éxecuter le jeu Wordle.
    """
    def __init__(self, wordlist, attempts = 5, debug = False):
        """
        Constructeur de la classe Wordle. 
        wordlist : liste de mots à deviner
        attempts : nombre de tentatives
        debug : affiche le mot secret si True
        """
        self.wordlist = wordlist
        self.secret_word = random.choice(self.wordlist)
        self.guesses = []
        self.attempts = attempts
        self.debug = debug

    def is_valid_word(self, word):
        """
        Vérifie si le mot est dans la liste de mots
        """
        if word in self.wordlist:
            return True
        else:
            return False
        
    def show_evalauation(self, evaluation):
        """
        Affiche les cases de couleurs du mot évalué
        """
        print(''.join(evaluation))
        
    def evaluate_guess(self, word):
        """
        Verifie les lettres bien placées et mal placées
        """
        evaluation = ['⬛' for i in range(len(self.secret_word))]
        secret_letters = list(self.secret_word)
        for i in range(len(self.secret_word)):
            if self.secret_word[i] == word[i]:
                evaluation[i] = '🟩'
                secret_letters[i] = None
        for i in range(len(self.secret_word)):
            if word[i] in secret_letters and evaluation[i] == '⬛':
                evaluation[i] = '🟨'
        return evaluation
    
    def play(self):
        """
        Fonction principale pour jouer au jeu Wordle. Utilisé pour gérer les tours et les tentatives. Limite le nombre de tentatives.
        """
        if self.debug:
            print(self.secret_word)
        while self.attempts != 0 and self.secret_word not in self.guesses:
            guess = input("Entrer un mot : ").upper()
            if guess not in self.wordlist:
                print("Le mot n'existe pas")
                continue
            self.show_evalauation(self.evaluate_guess(guess))
            self.attempts = self.attempts - 1
            self.guesses.append(guess)

        if self.secret_word in self.guesses:
            print("Félicitations ! Vous avez gagné(e), le mot était bien " + self.secret_word)
        else:
            print("Vous n'avez pas trouvé le mot... C'était " + self.secret_word)

def main():
    """
    Fonction principale. Utilisé pour initialiser le jeu et le lancer.
    """
    test = Wordle(words.wordlist, debug = True)
    test.play()

restart.restartEngine(main) # Permet de relancer le jeu si l'utilisateur le souhaite automatiquement
