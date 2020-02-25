from Etudiant import Etudiant
from Cours import Cours
from Note import Note
from functools import reduce

class BD_fmp:
    etudiantList = []
    coursList = []
    notesList = []

    #Etudiant Functions
    def addEtudiant(prenomEtu, nomEtu, niveauEtu):
        if not BD_fmp.containsEtudiant(prenomEtu, nomEtu, niveauEtu):
            BD_fmp.etudiantList.append(Etudiant(prenomEtu, nomEtu, niveauEtu))

    def containsEtudiantByNumero(numEtu):
        return BD_fmp.getIndexofEtudiantByNumero(numEtu)

    def containsEtudiant(prenomEtu, nomEtu, niveauEtu):
        return BD_fmp.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)

    def getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu):
        for etu in BD_fmp.etudiantList:
            if etu.prenomEtu == prenomEtu and etu.nomEtu == nomEtu and etu.niveauEtu == niveauEtu:
                return etu.numEtu
        return 0

    def getIndexofEtudiantByNumero(numEtu):
        for etu in BD_fmp.etudiantList:
            if etu.numEtu == numEtu:
                return etu.numEtu
        return 0

    def getListIndexofEtudiant(numEtu):
        iCount = -1
        for etu in BD_fmp.etudiantList:
            iCount = iCount + 1
            if etu.numEtu == numEtu:
                return iCount
        return -1

    def editEtudiant(prenomEtu, nomEtu, niveauEtu, newPrenom = None, newNom = None, newNiveau = None):
        if newPrenom is None and newNom is None and newNiveau is None:
            return False
        iIndex = BD_fmp.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        if not iIndex:
            return False
        iLstIndex = BD_fmp.getListIndexofEtudiant(iIndex)
        if iLstIndex < 0:
            return False
        if not (newPrenom is None):
            BD_fmp.etudiantList[iLstIndex].prenomEtu = newPrenom
        if not (newNom is None):
            BD_fmp.etudiantList[iLstIndex].nomEtu = newNom
        if not (newNiveau is None):
            BD_fmp.etudiantList[iLstIndex].niveauEtu = newNiveau
        return BD_fmp.etudiantList[iLstIndex].numEtu

    def removeEtudiantByEtudiant(prenomEtu, nomEtum, niveauEtu):
        numEtu = BD_fmp.getIndexofEtudiant(prenomEtu, nomEtum, niveauEtu)
        return BD_fmp.removeEtudiantByNumero(numEtu)

    def removeEtudiantByNumero(numEtu):
        iIndex = BD_fmp.getListIndexofEtudiant(numEtu)
        if not iIndex:
            return False
        BD_fmp.etudiantList.pop(iIndex)
        BD_fmp.removeNoteOfEtudiant(numEtu)
        return True

    def removeNoteOfEtudiant(numEtu):
        iCount = -1
        iIndexList = []
        for note in BD_fmp.notesList:
            iCount = iCount + 1
            if note.numEtu == numEtu:
                iIndexList.append(iCount)
        if len(iIndexList) < 1:
            return False
        for i in reversed(iIndexList):
            BD_fmp.notesList.pop(i)
        return True

    #Cours Functions
    def addCours(codeCours, intituleCours, niveauCours):
        if not BD_fmp.containsCours(codeCours, intituleCours, niveauCours):
            BD_fmp.coursList.append(Cours(codeCours, intituleCours, niveauCours))

    def containsCoursByCode(codeCours):
        return BD_fmp.getIndexofCoursByCode(codeCours)

    def containsCours(codeCours, intituleCours, niveauCours):
        return BD_fmp.getIndexofCours(codeCours, intituleCours, niveauCours)

    def getIndexofCours(codeCours, intituleCours, niveauCours):
        for cours in BD_fmp.coursList:
            if cours.codeCours == codeCours and cours.intituleCours == intituleCours and cours.niveauCours == niveauCours:
                return cours.codeCours
        return ""

    def getIndexofCoursByCode(codeCours):
        for cours in BD_fmp.coursList:
            if cours.codeCours == codeCours:
                return cours.codeCours
        return ""

    def getListIndexofCours(codeCours):
        iCount = -1
        for cours in BD_fmp.coursList:
            iCount = iCount + 1
            if cours.codeCours == codeCours:
                return iCount
        return -1

    def editCours(codeCours, intituleCours, niveauCours, newintitule = None, newNiveau = None):
        if newintitule is None and newNiveau is None:
            return False
        iIndex = BD_fmp.getIndexofCours(codeCours, intituleCours, niveauCours)
        if not iIndex:
            return False
        iLstIndex = BD_fmp.getListIndexofCours(iIndex)
        if iLstIndex < 0:
            return False
        if not (newintitule is None):
            BD_fmp.coursList[iLstIndex].intituleCours = newintitule
        if not (newNiveau is None):
            BD_fmp.coursList[iLstIndex].niveauCours = newNiveau
        return BD_fmp.coursList[iLstIndex].codeCours

    def removeCours(codeCours):
        if not BD_fmp.containsCoursByCode(codeCours):
            return False
        iIndex = BD_fmp.getListIndexofCours(codeCours)
        if not iIndex:
            return False
        BD_fmp.coursList.pop(iIndex)
        BD_fmp.removeNotesOfCours(codeCours)
        return True

    def removeNotesOfCours(codeCours):
        iCount = -1
        iIndexList = []
        for note in BD_fmp.notesList:
            iCount = iCount + 1
            if note.codeCours == codeCours:
                iIndexList.append(iCount)
        if len(iIndexList) < 1:
            return False
        for i in reversed(iIndexList):
            BD_fmp.notesList.pop(i)
        return True

    #Note Functions
    def addNoteByNumeroEtudiant(numEtu, codeCours, iNote):
        assert(iNote >= 0), "Note Should Be 0 or Greater"
        numEtu = BD_fmp.getIndexofEtudiantByNumero(numEtu)
        if numEtu <= 0:
            return "Etudiant Not Found!"
        codeCours = BD_fmp.getIndexofCoursByCode(codeCours)
        if codeCours == "":
            return "Cours Not Found!"
        if not BD_fmp.containsNote(numEtu, codeCours):
            BD_fmp.notesList.append(Note(numEtu, codeCours, iNote))
            return True
        return False

    def addNoteByEtudiant(prenomEtu, nomEtu, niveauEtu, codeCours, Note):
        numEtu = BD_fmp.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD_fmp.addNoteByNumeroEtudiant(numEtu, codeCours, Note)

    def containsNote(numEtu, codeCours):
        return BD_fmp.getListIndexofNote(numEtu, codeCours) > -1

    def getListIndexofNote(numEtu, codeCours):
        iCount = -1
        for note in BD_fmp.notesList:
            iCount = iCount + 1
            if note.numEtu == numEtu and note.codeCours == codeCours:
                return iCount
        return -1

    def editNoteByNumeroEtudiant(numEtu, codeCours, newNote):
        assert(newNote >= 0), "New Note Should be 0 or Greater!"
        if BD_fmp.containsNote(numEtu, codeCours):
            iIndex = BD_fmp.getListIndexofNote(numEtu, codeCours)
            BD_fmp.notesList[iIndex].Note = newNote
            return True
        return False

    def editNoteByEtudiant(prenomEtu, nomEtu, niveauEtu, codeCours, newNote):
        numEtu = BD_fmp.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD_fmp.editNoteByNumeroEtudiant(numEtu, codeCours, newNote)

    def removeNoteByNumeroEtudiant(numEtu, codeCours):
        if BD_fmp.containsNote(numEtu, codeCours):
            iIndex = BD_fmp.getListIndexofNote(numEtu, codeCours)
            if not iIndex:
                return False
            BD_fmp.notesList.pop(iIndex)
            return True
        return False

    def removeNoteByEtudiant(prenomEtu, nomEtu, niveauEtu, codeCours):
        numEtu = BD_fmp.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD_fmp.removeNoteByNumeroEtudiant(numEtu, codeCours)

    # Average Functions
    def averageOfClass(codeCours):
        iCount = 0
        iSum = 0
        if not BD_fmp.containsCoursByCode(codeCours):
            return -1
        for note in BD_fmp.notesList:
            if note.codeCours == codeCours:
                iCount = iCount + 1
                iSum = iSum + note.note
        if iCount > 0:
            return iSum / iCount
        return 0

    def averageOfClassByfmp(codeCours):
        if not BD_fmp.containsCoursByCode(codeCours):
            return -1
        notesOfPassedCourse = list(map(lambda x: x.note, list(filter(lambda x: x.codeCours == codeCours, BD_fmp.notesList))))
        return reduce(lambda x, y: x + y, notesOfPassedCourse) / len(notesOfPassedCourse)
        # return 0

    def averageOfEtudiantByfmp(numEtu):
        notesOfEtudiant = list(map(lambda x: x.note, list(filter(lambda x: x.numEtu == numEtu, BD_fmp.notesList))))
        return reduce(lambda a, b: (a + b), notesOfEtudiant) / len(notesOfEtudiant)

    def averageOfEtudiantByEtudiantByfmp(prenomEtu, nomEtu, niveauEtu):
        numEtu = BD_fmp.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD_fmp.averageOfEtudiantByfmp(numEtu)

    def averageOfStudent(numEtu):
        iCount = 0
        iSum = 0
        if not BD_fmp.containsEtudiant():
            return -1
        for note in BD_fmp.notesList:
            if note.numEtu == numEtu:
                iCount = iCount + 1
                iSum = iSum + note.note
        if iCount > 0:
            return iSum / iCount
        return 0

    def averageOfStudentByEtudiant(prenomEtu, nomEtu, niveauEtu):
        numEtu = BD_fmp.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu)
        return BD_fmp.averageOfStudent(numEtu)

    def ConsultCours(codeCours):
        return list(map(lambda x: x.note, list(filter(lambda x: x.codeCours == codeCours, BD_fmp.notesList))))

    def ConsultEtudiantByNumero(numEtu):
        return list(map(lambda x: x.note, list(filter(lambda x: x.numEtu == numEtu, BD_fmp.notesList))))

    def ConsultEtudiantByEtudiant(prenomEtu, nomEtu, niveauEtu):
        return BD_fmp.ConsultEtudiantByNumero(BD_fmp.getIndexofEtudiant(prenomEtu, nomEtu, niveauEtu))

if __name__ == "__main__":
    BD_fmp.addEtudiant("Charbel", "Farah", Etudiant.cycleC)
    BD_fmp.addEtudiant("Elio", "Wehbe", Etudiant.cycleC)
    BD_fmp.addEtudiant("Christopher", "Daccache", Etudiant.cycleC)
    BD_fmp.addEtudiant("fgasfas", "fasfsa", Etudiant.cycleC)
    BD_fmp.addEtudiant("gasdgdw", "asda", Etudiant.cycleC)
    BD_fmp.addEtudiant("fqdfq", "gfege", Etudiant.cycleC)

    # print(*BD_fmp.etudiantList)

    BD_fmp.addCours("UTC503", "Paradigme De Programmation", Cours.nivC)
    BD_fmp.addCours("NFP121", "Programmation Avancee", Cours.nivC)
    BD_fmp.addCours("UTC501", "SI", Cours.nivC)

    # print(*BD_fmp.coursList)

    BD_fmp.addNoteByEtudiant("Charbel", "Farah", Etudiant.cycleC, "UTC503", 15)
    BD_fmp.addNoteByEtudiant("Elio", "Wehbe", Etudiant.cycleC, "UTC503", 13)
    BD_fmp.addNoteByEtudiant("Christopher", "Daccache", Etudiant.cycleC, "UTC503", 12)
    BD_fmp.addNoteByEtudiant("fgasfas", "fasfsa", Etudiant.cycleC, "UTC503", 5)
    BD_fmp.addNoteByEtudiant("gasdgdw", "asda", Etudiant.cycleC, "UTC503", 3)
    BD_fmp.addNoteByEtudiant("fqdfq", "gfege", Etudiant.cycleC, "UTC503", 1)

    BD_fmp.addNoteByEtudiant("Charbel", "Farah", Etudiant.cycleC, "NFP121", 15)
    BD_fmp.addNoteByEtudiant("Elio", "Wehbe", Etudiant.cycleC, "NFP121", 18)
    BD_fmp.addNoteByEtudiant("Christopher", "Daccache", Etudiant.cycleC, "NFP121", 13)
    BD_fmp.addNoteByEtudiant("fgasfas", "fasfsa", Etudiant.cycleC, "NFP121", 11)
    BD_fmp.addNoteByEtudiant("gasdgdw", "asda", Etudiant.cycleC, "NFP121", 9)
    BD_fmp.addNoteByEtudiant("fqdfq", "gfege", Etudiant.cycleC, "NFP121", 6)

    BD_fmp.addNoteByEtudiant("Charbel", "Farah", Etudiant.cycleC, "UTC504", 10)
    BD_fmp.addNoteByEtudiant("Charbel", "Farah", Etudiant.cycleC, "UTC505", 12)
    BD_fmp.addNoteByEtudiant("Charbel", "Farah", Etudiant.cycleC, "UTC502", 14)
    BD_fmp.addNoteByEtudiant("Charbel", "Farah", Etudiant.cycleC, "UTC501", 13)

    # print(len(BD_fmp.notesList))
    # print(*BD_fmp.notesList)
    # print(len(BD_fmp.notesList))

    # print(BD_fmp.averageOfClassByfmp("UTC503"))
    # print(BD_fmp.averageOfClassByfmp("NFP121"))

    # print(BD_fmp.ConsultCours("UTC503"))
    # print(BD_fmp.ConsultCours("NFP121"))

    # print(BD_fmp.averageOfEtudiantByEtudiantByfmp("Charbel", "Farah", Etudiant.cycleC))
    # print(BD_fmp.averageOfEtudiantByfmp(1))

    print(reduce(lambda a, b: a + b, list(map(lambda x: x.note, list(filter(lambda x: x.codeCours == "UTC503", BD_fmp.notesList))))) / len(list(filter(lambda x: x.codeCours == "UTC503", BD_fmp.notesList))))

    # print(BD_fmp.ConsultEtudiantByNumero(1))
    # print(BD_fmp.ConsultEtudiantByEtudiant("Charbel", "Farah", Etudiant.cycleC))
