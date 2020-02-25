class Cours:
    # codeCours
    # intituleCours
    # niveauCours #A, B ou C
    nivA = "A"
    nivB = "B"
    nivC = "C"
    def __init__(this, codeCours, intituleCours, niveauCours):
        this.codeCours = codeCours
        this.intituleCours = intituleCours
        this.niveauCours = niveauCours

    def __str__(this):
        return "Code: " + this.codeCours + "\n" + "intitule: " + this.intituleCours + "\n" + "Niveau: " + this.niveauCours
