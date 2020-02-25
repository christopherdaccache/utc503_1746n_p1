class Note:
    # numEtu
    # codeCours
    # note
    def __init__(this, numEtu, codeCours, note):
        this.numEtu = numEtu
        this.codeCours = codeCours
        this.note = note

    def __str__(this):
        return "Numero Etudiant: " + str(this.numEtu) + "\n" + "Code Cours: " + this.codeCours + "\n" + "note: " + str(this.note)
