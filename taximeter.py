# Welcome on my open source taximeter.

# Classe qui gére les distances.
class Distance:
    def __init__(self, valeur):
        self.valeur = valeur

    def get_valeur(self):
        return self.valeur


# Classe qui gère les temps.
class Temps:
    def __init__(self, valeur):
        self.valeur = valeur

    def get_valeur(self):
        return self.valeur


# Classe qui gère les tarifs.
class Tarif:
    def __init__(self, valeur):
        self.valeur = valeur

    def get_valeur(self):
        return self.valeur


# Fonction pour calculer le temps automatiquement à partir de la distance et d'une vitesse moyenne.
def calcul_temps(distance, vitesse_moyenne=50):
    if vitesse_moyenne <= 0:
        raise ValueError("La vitesse moyenne doit être supérieure à zéro.")
    return distance / vitesse_moyenne  # Temps en heures.


# Fonction pour calculer le tarif en fonction de la distance.
def calcul_tarif(distance, vitesse_moyenne=50):
    temps = calcul_temps(distance, vitesse_moyenne)
    tarif_distance = distance * 0.5  # Exemple : 0.5 $ par kilomètre.
    tarif_temps = temps * 5  # Exemple : 5 $ par heure.
    return tarif_distance + tarif_temps, vitesse_moyenne, temps


# Code pour démarrer le script.
def main():
    print("Taximeter.py - Version console - Build by: Nox")
    print("-------------------------------")

    try:
        distance = float(input("Entrez la distance parcourue en kilomètres : "))
        vitesse_moyenne = 50  # Vitesse moyenne en km/h.

        tarif, vitesse, temps = calcul_tarif(distance, vitesse_moyenne)

        print(f"Vitesse moyenne utilisée : {vitesse:.2f} km/h")
        print(f"Temps estimé : {temps:.2f} heures")
        print(f"Tarif : {tarif:.2f} $")
    except ValueError:
        print("Erreur : veuillez entrer une distance valide.")


if __name__ == "__main__":
    main()
