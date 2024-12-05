"""gère l'affichage lors de la modification d'une liste
"""
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class ModificationListeView (AbstractView) :
    """gère l'affichage lors de la modification d'une liste
    """
    def __init__(self):
        self.__questions = inquirer.select(
            message='Que souhaites tu faire maintenant?'
            , choices=[
                Choice('Ajouter un mot')
                ,Choice('Supprimer un mot')
                ,Choice("Retour à l'accueil")
                ]
        )

    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse== 'Ajouter un mot':
            from view.ajoutermotview import AjouterMotView
            return AjouterMotView()
        if reponse== 'Supprimer un mot':
            from view.supprimermotview import SupprimerMotView
            return SupprimerMotView()
        #elif reponse== "Retour à l'accueil":
        from view.accueilpersoview import AccueilPersoView
        return AccueilPersoView()
