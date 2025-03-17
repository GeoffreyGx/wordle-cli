#
# Restart Library
# Une librairie pour redémarrer automatiquement une fonction 
# Créée par Geoffrey Gambicchia
#

def restart(function):
    """
    Redémarre n'importe quel fonction automatiquement
    """
    function()
    while ask_restart() == True:
        function()


def ask_restart():
    """
    Demande à l'utilisateur si il souhaite redémarrer
    """
    liste = ["oui", "yes", "ok", "1", "o", "y"]
    rep = input("Voulez-vous recommencer ? [y/N]: ").lower()
    if rep in liste:
        return True
    else:
        print('A bientôt 👋')
