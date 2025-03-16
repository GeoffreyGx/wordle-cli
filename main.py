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
        self.alphabet = Alphabet()
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
        for char in evaluation:
            print(char, end='')
        print() # Ajoute un retour à la ligne


    def evaluate_guess(self, word):
        """
        Verifie les lettres bien placées et mal placées
        """
        evaluation = ['⬛' for i in range(len(self.secret_word))]
        secret_letters = [char for char in self.secret_word]
        for i in range(len(self.secret_word)):
            if self.secret_word[i] == word[i]:
                evaluation[i] = '🟩'
                secret_letters[i] = None
                self.alphabet.set_green(word[i])
        for i in range(len(self.secret_word)):
            if word[i] in secret_letters and evaluation[i] == '⬛':
                evaluation[i] = '🟨'
                self.alphabet.set_yellow(word[i])
        return evaluation

    def play(self):
        """
        Fonction principale pour jouer au jeu Wordle. 
        Utilisé pour gérer les tours et les tentatives. Limite le nombre de tentatives.
        """
        if self.debug:
            print(self.secret_word)
        while self.attempts != 0 and self.secret_word not in self.guesses:
            guess = input("Entrer un mot : ").upper()
            if guess not in self.wordlist:
                print("Le mot n'existe pas")
                continue
            self.show_evalauation(self.evaluate_guess(guess))
            print(self.alphabet)
            self.attempts = self.attempts - 1
            self.guesses.append(guess)

        if self.secret_word in self.guesses:
            print("Félicitations ! Vous avez gagné(e), le mot était bien " + self.secret_word)
        else:
            print("Vous n'avez pas trouvé le mot... C'était " + self.secret_word)

class Alphabet:
    """
    Alphabet class. Utilisé pour garder une trace des lettres utilisés et bien placées.
    """
    def __init__(self):
        """
        Constructeur de la classe Alphabet.
        Ne prend aucun argument. Initialise l'alphabet et un dictionnaire lettres utilisées.
        """
        self.alphabet = [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.used = {}

    def set_green(self, letter):
        """
        Change le statut de la lettre en vert
        """
        self.used[letter] = "green"

    def set_yellow(self, letter):
        """
        Change le statut de la lettre en jaune
        """
        self.used[letter] = "yellow"

    def __str__(self):
        """
        Permet d'afficher l'alphabet avec les lettres utilisées et leur statut
        """
        string = ""
        for letter in self.alphabet:
            if letter in self.used:
                if self.used[letter] == "green":
                    string += letter + "-> 🟩  "
                elif self.used[letter] == "yellow":
                    string += letter + "-> 🟨  "
            else:
                string += letter + "->⬛  "
        return string

def main():
    """
    Fonction principale. Utilisé pour initialiser le jeu et le lancer.
    """
    test = Wordle(words.wordlist, debug = True)
    test.play()

restart.restartEngine(main) # Permet de relancer le jeu si l'utilisateur le souhaite automatiquement
