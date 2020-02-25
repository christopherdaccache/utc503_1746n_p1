from Etudiant import Etudiant
from Cours import Cours
from Note import Note

class BD:
    etudiantList = []
    coursList = []
    notesList = []

    #Etudiant Functions
    def addEtudiant(prenomEtu, nomEtu, niveauEtu):
        if not BD.containsEtudiant(prenomEtu, nomEtu, niveauEtu):
            BD.etudiantList.append(Etudiant(prenomEtu, nomEtu, niveauEtu))

    def containsEtudiantByNumero(numEtu):
        return BD.getIndexofEtudiantByNumero(numEtu)

    def containsEtudiant(prenomEtu, nomEtu, niveauEtu):
        return BD.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)

    def getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu):
        for etu in BD.etudiantList:
            if etu.prenomEtu == prenomEtu and etu.nomEtu == nomEtu and etu.niveauEtu == niveauEtu:
                return etu.numEtu
        return 0

    def getIndexofEtudiantByNumero(numEtu):
        for etu in BD.etudiantList:
            if etu.numEtu == numEtu:
                return etu.numEtu
        return 0

    def getListIndexofEtudiant(numEtu):
        iCount = -1
        for etu in BD.etudiantList:
            iCount = iCount + 1
            if etu.numEtu == numEtu:
                return iCount
        return -1

    def editEtudiant(prenomEtu, nomEtu, niveauEtu, newPrenom = None, newNom = None, newNiveau = None):
        if newPrenom is None and newNom is None and newNiveau is None:
            return False
        iIndex = BD.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        if not iIndex:
            return False
        iLstIndex = BD.getListIndexofEtudiant(iIndex)
        if iLstIndex < 0:
            return False
        if not (newPrenom is None):
            BD.etudiantList[iLstIndex].prenomEtu = newPrenom
        if not (newNom is None):
            BD.etudiantList[iLstIndex].nomEtu = newNom
        if not (newNiveau is None):
            BD.etudiantList[iLstIndex].niveauEtu = newNiveau
        return BD.etudiantList[iLstIndex].numEtu

    def removeEtudiantByEtudiant(prenomEtu, nomEtum, niveauEtu):
        numEtu = BD.getIndexofEtudiant(prenomEtu, nomEtum, niveauEtu)
        return BD.removeEtudiantByNumero(numEtu)

    def removeEtudiantByNumero(numEtu):
        iIndex = BD.getListIndexofEtudiant(numEtu)
        if not iIndex:
            return False
        BD.etudiantList.pop(iIndex)
        BD.removeNoteOfEtudiant(numEtu)
        return True

    def removeNoteOfEtudiant(numEtu):
        iCount = -1
        iIndexList = []
        for note in BD.notesList:
            iCount = iCount + 1
            if note.numEtu == numEtu:
                iIndexList.append(iCount)
        if len(iIndexList) < 1:
            return False
        for i in reversed(iIndexList):
            BD.notesList.pop(i)
        return True

    #Cours Functions
    def addCours(codeCours, intituleCours, niveauCours):
        if not BD.containsCours(codeCours, intituleCours, niveauCours):
            BD.coursList.append(Cours(codeCours, intituleCours, niveauCours))

    def containsCours(codeCours):
        return BD.getIndexofCoursByCode(codeCours)

    def containsCours(codeCours, intituleCours, niveauCours):
        return BD.getIndexofCours(codeCours, intituleCours, niveauCours)

    def getIndexofCours(codeCours, intituleCours, niveauCours):
        for cours in BD.coursList:
            if cours.codeCours == codeCours and cours.intituleCours == intituleCours and cours.niveauCours == niveauCours:
                return cours.codeCours
        return ""

    def getIndexofCoursByCode(codeCours):
        for cours in BD.coursList:
            if cours.codeCours == codeCours:
                return cours.codeCours
        return ""

    def getListIndexofCours(codeCours):
        iCount = -1
        for cours in BD.coursList:
            iCount = iCount + 1
            if cours.codeCours == codeCours:
                return iCount
        return -1

    def editCours(codeCours, intituleCours, niveauCours, newintitule = None, newNiveau = None):
        if newintitule is None and newNiveau is None:
            return False
        iIndex = BD.getIndexofCours(codeCours, intituleCours, niveauCours)
        if not iIndex:
            return False
        iLstIndex = BD.getListIndexofCours(iIndex)
        if iLstIndex < 0:
            return False
        if not (newintitule is None):
            BD.coursList[iLstIndex].intituleCours = newintitule
        if not (newNiveau is None):
            BD.coursList[iLstIndex].niveauCours = newNiveau
        return BD.coursList[iLstIndex].codeCours

    def removeCours(codeCours):
        if not BD.containsCours(codeCours):
            return False
        iIndex = BD.getListIndexofCours(codeCours)
        if not iIndex:
            return False
        BD.coursList.pop(iIndex)
        BD.removeNotesOfCours(codeCours)
        return True

    def removeNotesOfCours(codeCours):
        iCount = -1
        iIndexList = []
        for note in BD.notesList:
            iCount = iCount + 1
            if note.codeCours == codeCours:
                iIndexList.append(iCount)
        if len(iIndexList) < 1:
            return False
        for i in reversed(iIndexList):
            BD.notesList.pop(i)
        return True

    #Note Functions
    def addNoteByNumeroEtudiant(numEtu, codeCours, Note):
        assert(Note >= 0), "Note Should Be 0 or Greater"
        numEtu = BD.getIndexofEtudiantByNumero(numEtu)
        if numEtu <= 0:
            return "Etudiant Not Found!"
        codeCours = BD.getIndexofCoursByCode(codeCours)
        if codeCours == "":
            return "Cours Not Found!"
        if BD.containsNote(numEtu, codeCours) < 0:
            BD.notesList.append(numEtu, codeCours, Note)
            return True
        return False

    def addNoteByEtudiant(prenomEtu, nomEtu, niveauEtu, codeCours, Note):
        numEtu = BD.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD.addNoteByNumeroEtudiant(numEtu, codeCours, Note)

    def containsNote(numEtu, codeCours):
        return BD.getListIndexofNote(numEtu, codeCours) > -1

    def getListIndexofNote(numEtu, codeCours):
        iCount = -1
        for note in BD.notesList:
            iCount = iCount + 1
            if note.numEtu == numEtu and note.codeCours == codeCours:
                return iCount
        return -1

    def editNoteByNumeroEtudiant(numEtu, codeCours, newNote):
        assert(newNote >= 0), "New Note Should be 0 or Greater!"
        if BD.containsNote(numEtu, codeCours):
            iIndex = BD.getListIndexofNote(numEtu, codeCours)
            BD.notesList[iIndex].Note = newNote
            return True
        return False

    def editNoteByEtudiant(prenomEtu, nomEtu, niveauEtu, codeCours, newNote):
        numEtu = BD.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD.editNoteByNumeroEtudiant(numEtu, codeCours, newNote)

    def removeNoteByNumeroEtudiant(numEtu, codeCours):
        if BD.containsNote(numEtu, codeCours):
            iIndex = BD.getListIndexofNote(numEtu, codeCours)
            if not iIndex:
                return False
            BD.notesList.pop(iIndex)
            return True
        return False

    def removeNoteByEtudiant(prenomEtu, nomEtu, niveauEtu, codeCours):
        numEtu = BD.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD.removeNoteByNumeroEtudiant(numEtu, codeCours)

    # Average Functions
    def averageOfClass(codeCours):
        iCount = 0
        iSum = 0
        if not BD.containsCours(codeCours):
            return -1
        for note in BD.notesList:
            if note.codeCours == codeCours:
                iCount = iCount + 1
                iSum = iSum + note.note
        if iCount > 0:
            return iSum / iCount
        return 0

    def averageOfStudent(numEtu):
        iCount = 0
        iSum = 0
        if not BD.containsEtudiant():
            return -1
        for note in BD.notesList:
            if note.numEtu == numEtu:
                iCount = iCount + 1
                iSum = iSum + note.note
        if iCount > 0:
            return iSum / iCount
        return 0

    def averageOfStudentByEtudiant(prenomEtu, nomEtu, niveauEtu):
        numEtu = BD.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD.averageOfStudent(numEtu)

    def ConsultCours(codeCours):
        return list(map(lambda x: x.note, list(filter(lambda x: x.codeCours == codeCours, BD.notesList))))

    def ConsultEtudiantByNumero(numEtu):
        return list(map(lambda x: x.note, list(filter(lambda x: x.numEtu == numEtu, BD.notesList))))

    def ConsultEtudiantByEtudiant(prenomEtu, nomEtu, niveauEtu):
        return BD.ConsultEtudiantByNumero(BD.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu))