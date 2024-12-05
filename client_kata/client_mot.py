"""couche service: gère les requetes des Mots vers l'API
"""

import re #import regex
import requests

from utils.singleton import Singleton


from client_liste import ClientListe
from client_joueur import ClientJoueur
END_POINT="/mot"

#pylint: disable=invalid-name
#justification: le __HOST pourrait reservir pour un déploiement
#pylint: disable=no-self-use
#justification: self use dans d'autres fichiers

class ClientMot(metaclass= Singleton):
    """gère le endpoint pour les mots
    """
    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"

    def create_mot(self, mot: str) :
        '''Ajouter un mot dans la bdd

        Parameters
        mot : str
        '''
        #pylint: disable=unused-variable
        #justification: nécessaire pour lancer la requete
        req = requests.post(f"{self.__HOST}{END_POINT}/contenu/{mot}")


    def add_mot_to_liste(self, mot : str, nom_liste : str, id_joueur : int) :
        """Ajoute un mot à une liste personelle d'un joueur

        Parameters :
        mot : str
        nom_liste : str
        id_joueur : int

        Returns
        Renvoie True si le mot a bien été ajouté à la liste. S'il n'a pas été ajouté, cela veut dire
        que le mot était déjà dans la liste où qu'il ne respectait pas les conditions"""

        #On vérifie si le mot est déjà dans la base de données
        regex = "^[A-zÀ-ú]+$"
        resultat = re.match(regex, mot)
        if resultat is None:
            print(f"Le mot {mot} ne respecte pas les conditions: uniquement des lettres avec ou "
                  "sans accents, pas de chiffres, pas de caractères spéciaux ")
            return False
        if len(mot)>50:
            print(f"Le mot {mot} est trop long ")
            return False
        # from client_mot import ClientMot
        clientmot = ClientMot()

        if clientmot.get_id(mot) is None :
            clientmot.create_mot(mot)
        id_mot = clientmot.get_id(mot)

        #On vérifie si le mot est déjà dans la liste

        #id_joueur = (Session().joueur.id_joueur)
        # from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        # from business_objects.liste import Liste
        listes = clientjoueur.get_listes(id_joueur)
        for liste in listes :
            if liste.nom == nom_liste :
                liste_d_ajout = liste

        if mot in liste_d_ajout.liste :
            print(f"Le mot {mot} est déjà dans la liste")
            return False

        # from client_liste import ClientListe
        clientliste = ClientListe()
        clientliste.ajouter_mot(liste_d_ajout.id_liste, id_mot)
        return True



    def get_id(self, mot) :
        '''Retourne l'id du mot (s'il existe dans la bdd)

        Parameters :
        mot : str

        Returns :
        L'id du mot ou None
        '''
        req = requests.get(f"{self.__HOST}{END_POINT}/mot/{mot}")
        if isinstance(req.json(), int):
            return req.json()
        return None
