def restartEngine(function):
    function()
    while restart() == True:
        function()


def restart():
    liste = ["OUI","oui","Oui","YES","Yes","yes","OK","ok","1","o"]
    rep = input("Voulez-vous recommencer ? : ")
    if rep in liste:
        return True
    else:
        print('Au revoir')
