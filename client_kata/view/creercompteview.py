"""gère l'affichage pour créer un compte
"""
import re
from InquirerPy import inquirer

from view.abstractview import AbstractView


ASK_PSEUDO=inquirer.text(message = 'Entre un pseudo')

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)

class CreerCompteView(AbstractView):
    """gère l'affichage pour créer un compte
    """


    def display_info(self):
        print("Création du compte")

    def make_choice(self):
        pseudo = ASK_PSEUDO.execute()
        reg_exp = r'\w+'
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        if re.fullmatch(reg_exp, pseudo) is None :
            print("Le pseudo n'est pas autorisé. Seuls les lettres et les chiffres sont autorisés")
        else :
            if clientjoueur.get_id(pseudo) is None :
                #Le joueur est inséré dans la base de données
                clientjoueur.create_joueur(pseudo = pseudo)
            else :
                #Message d'erreur
                print("Le pseudo existe déjà")
        #Dans tous les cas, on revient ensuite à l'écran d'accueil
        from view.accueilkataview import AccueilKataView
        return AccueilKataView()
