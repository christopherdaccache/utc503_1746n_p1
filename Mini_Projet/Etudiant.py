class Etudiant:
    nbrEtu = 0
    # numEtu
    # prenomEtu
    # nomEtu
    # niveauEtu #cycle d'inscription : A, B ou C
    cycleA = "A"
    cycleB = "B"
    cycleC = "C"
    def __init__(this, prenomEtu, nomEtu, niveauEtu):
        Etudiant.nbrEtu = Etudiant.nbrEtu + 1
        this.numEtu = Etudiant.nbrEtu
        this.prenomEtu = prenomEtu
        this.nomEtu = nomEtu
        this.niveauEtu = niveauEtu
    
    def __str__(this):
        return "ID Etudiant: " + str(this.numEtu) + "\n" + "Prenom: " + this.prenomEtu + "\n" + "Nom: " + this.nomEtu + "\n" + "Niveau: " + this.niveauEtu
    