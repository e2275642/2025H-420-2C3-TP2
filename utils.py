# utils.py

import csv
import json

def lire_csv(chemin):
    lignes = []
    with open("fichier_csv", 'r', encoding='utf-8') as f:
        lecteur = csv.reader(f)
        for ligne in lecteur:
            dictionnaire= {}
            for i in range(len(ligne)):
                dictionnaire[str(i + 1)] = ligne[i]
            lignes.append(dictionnaire)
        return lignes

"""Lire un fichier CSV et retourner la liste des lignes.
    Chaque dictionnaire correspond à une ligne du fichier.
    """
pass

def sauvegarder_json(data, chemin):

    with open(chemin, mode='w', encoding='utf-8') as fichier:
        json.dump(data, fichier)

    """
    Sauvegarder des données dans un fichier JSON.
    - data : un objet Python (par exemple, un dictionnaire ou une liste)
    - chemin : chemin du fichier JSON à écrire
    Utiliser json.dump avec indentation pour que le fichier soit lisible.
    """
    pass

def ecrire_texte(contenu, chemin):
    with open(chemin, mode='w', encoding='utf-8') as fichier:
        fichier.write(contenu)

    """
    Écrire du texte brut dans un fichier texte (.txt).
    - contenu : texte à écrire
    - chemin : chemin du fichier texte à créer
    """
    pass
