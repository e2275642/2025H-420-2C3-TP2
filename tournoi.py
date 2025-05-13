# tournoi.py

from joueur import Joueur
from match import Match
import utils

class Tournoi:
    def __init__(self, nom):
        """
        Initialise un tournoi avec son nom.
        Initialise aussi une liste vide pour les joueurs et pour les matchs.
        """
        self.nom = nom
        self.joueurs = []
        self.matchs = []


def charger_joueurs(self,chemin_csv):
    import csv
    import joueur
    joueurs = []
    with open("joueurs.csv", "r", encoding='utf-8') as f:
        lecteur = csv.reader(f)
        for ligne in lecteur:
                print(ligne)

        joueurs = self.charger_joueurs("joueurs.csv")
        for joueur in joueurs:
                print(joueur)
        pass

    def charger_matchs(self, chemin_csv):
        """
        Lire un fichier CSV contenant les matchs.
        Chaque ligne contient deux pseudos de joueurs (joueur1, joueur2).
        Trouver les objets Joueur correspondants dans la liste de joueurs.
        Pour chaque ligne, créer un objet Match et l'ajouter à la liste des matchs.
        Utiliser la fonction lire_csv() du fichier utils.py.
        """
        import csv
        matchs = []
        with open("matchs.csv", newline='', encoding='utf-8') as f:
            lecteur = csv.reader(f)
            for ligne in lecteur:
                if ligne:
                    id_j1 = int(ligne[0])
                    id_j2 = int(ligne[1])
                    score1 = int(ligne[2])
                    score2 = int(ligne[3])

                    joueur1 = joueurs[id_j1 - 1]
                    joueur2 = joueurs[id_j2 - 1]

                    if joueur1 and joueur2:
                        match = Match(joueur1, joueur2)
                        match.definir_scores(score1, score2)
                        matchs.append(match)
                    else:
                        print("mauvais matchup")
        return matchs
        pass
        

    def saisir_scores(self):
        """
        Pour chaque match dans la liste des matchs :
        - Afficher le match (afficher les pseudos des deux joueurs)
        - Demander à l'utilisateur d'entrer les deux scores (score du joueur 1, score du joueur 2)
        - Enregistrer les scores dans l'objet Match
        - Déterminer le gagnant du match
        - Si un gagnant existe (pas d'égalité), appeler enregistrer_victoire() sur le joueur gagnant.
        """
        for match in self.matchs:
            print(f"Match: {match.joueur1} vs {match.joueur2}")
            try:
                score1 = int(input(f"Entrez le score de {match.joueur1}: "))
                score2 = int(input(f"Entrez le score de {match.joueur2}: "))
                match.definir_scores(score1, score2)
                if score1 > score2:
                    gagnant = next((j for j in self.joueurs if j.pseudo == match.joueur1), None)
                    if gagnant:
                        gagnant.enregistrer_victoire()
                elif score2 > score1:
                    gagnant = next((j for j in self.joueurs if j.pseudo == match.joueur2), None)
                    if gagnant:
                        gagnant.enregistrer_victoire()
            except ValueError:
                print("Erreur : Veuillez entrer des scores valides.")

    def afficher_classement(self):
        """
        Afficher le classement des joueurs.
        Classer les joueurs du plus grand nombre de victoires au plus petit.
        Afficher leur pseudo et leur nombre de victoires.
        """
        self.joueurs.sort(key=lambda j: j.victoires, reverse=True)
        print("Classement des joueurs :")
        for joueur in self.joueurs:
            print(f"{joueur.pseudo} - Victoires : {joueur.victoires}")

    def sauvegarder(self, chemin_json):
        """
        Sauvegarder le tournoi dans un fichier JSON.
        Le fichier doit contenir :
        - le nom du tournoi
        - la liste des joueurs (convertis en dictionnaires à l'aide de la fonction to_dict déjà implémenté dans la classe Joueur)
        Utiliser la fonction sauvegarder_json() du fichier utils.py.
        """

        def convertir_json(tournoi1, joueurs, matchs):
            return {
                "nom":tournoi1,
                "joueurs":[j.to_dict() for j in joueurs],
                "matchs": [
                    {
                        "joueur1": m.joueur1.pseudo,
                        "joueur2": m.joueur2.pseudo,
                        "score1": m.score1,
                        "score2": m.score2,
                        "gagnant": (
                            m.gagnant().pseudo if m.gagnant() else "None"
                        )
                    }
                    for m in matchs
                ]
            }

        import json

        def save_tournoi_json(nom_fichier, nom_tournoi, joueurs, matchs):
            data =convertir_json(nom_tournoi, joueurs, matchs)
            with open(nom_fichier, 'w', encoding='utf-8') as f:
                json.dump(data, f)

        pass

    def generer_rapport(self, chemin_texte):
        """
        Générer un rapport du tournoi sous forme de fichier texte.
        Le rapport doit contenir :
        - Le nom du tournoi
        - La liste des matchs joués avec leurs scores
        - Le classement final
        Utiliser la fonction ecrire_texte() du fichier utils.py.
        """





    pass
