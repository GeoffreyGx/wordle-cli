import random # Utilisé pour séléctionner un mot dans la liste
import restart # Outil pour redémarrer le jeu automatiquement
import words # Liste des mots

class Wordle:
    """
    Wordle game class. Utilisé pour jouer et éxecuter le jeu Wordle.
    """
    def __init__(self, wordlist, attempts = 6, debug = False):
        """
        Constructeur de la classe Wordle. 
        wordlist : liste de mots à deviner
        attempts : nombre de tentatives
        debug : affiche le mot secret si True
        """
        self.wordlist = wordlist
        self.secret_word = random.choice(self.wordlist)
        self.guesses = [] # Liste des mots déjà essayés
        self.alphabet = Alphabet()
        self.max_attempts = attempts
        self.attempts = attempts
        self.debug = debug

    def show_evaluation(self, evaluation):
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
        for i in range(len(self.secret_word)): # Vérifie les lettres bien placées
            if word[i] == self.secret_word[i]:
                evaluation[i] = '🟩'
                secret_letters[i] = None
                if word[i] not in secret_letters:
                    self.alphabet.remove_letter(word[i])
        for i in range(len(self.secret_word)): # Vérifie les lettres mal placées mais existantes
            if word[i] in secret_letters and evaluation[i] == '⬛':
                evaluation[i] = '🟨'
        for i in range(len(self.secret_word)): # Vérifie les lettres inexistante
            if word[i] not in secret_letters:
                self.alphabet.remove_letter(word[i])
        return evaluation

    def play(self):
        """
        Fonction principale pour jouer au jeu Wordle. 
        Utilisé pour gérer les tours et les tentatives. Limite le nombre de tentatives.
        """
        print(f'Bienvenue sur le Wordle.\nVous devez deviner le mot en {self.max_attempts} coups!')
        if self.debug:
            print(self.secret_word)
        while self.attempts != 0 and self.secret_word not in self.guesses: # Boucle tant que le mot n'est pas trouvé et qu'il reste des tentatives
            guess = input(f"Entrer un mot ({self.max_attempts - self.attempts + 1}/{self.max_attempts}): ").upper()
            if len(guess) != len(self.secret_word):
                print("Le mot doit avoir une longueur de " + str(len(self.secret_word)) + " lettres")
            elif guess not in self.wordlist:
                print("Le mot n'existe pas")
            else:
                self.show_evaluation(self.evaluate_guess(guess))
                print(self.alphabet)
                self.attempts = self.attempts - 1
                self.guesses.append(guess)
            print() # Ajoute un retour un ligne

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
        self.status = {}

    def remove_letter(self, letter):
        """
        Change le statut de la lettre en jaune
        """
        self.status[letter] = "inactive"

    def __str__(self):
        """
        Permet d'afficher l'alphabet avec les lettres utilisées et leur statut
        """
        string = ""
        for letter in self.alphabet:
            if letter in self.status:
                if self.status[letter] == "inactive":
                    string += "  "
            else:
                string += letter + " "
        return string

def main():
    """
    Fonction principale. Utilisé pour initialiser le jeu et le lancer.
    """
    test = Wordle(words.wordlist)
    test.play()

restart.restart(main) # Permet de relancer le jeu si l'utilisateur le souhaite automatiquement
