from Etudiant import Etudiant
from Cours import Cours
from Note import Note
from BD import BD

list = [1,2,3,4]
list.pop(2)

#Test Etudiant
def testEtudiant():
    print(" Test Etudiant!")
    BD.addEtudiant("toni", "abifarah", Etudiant.cycleA)
    # print(*BD.etudiantList)
    print(BD.containsEtudiant("toni", "khoury", Etudiant.cycleA))
    print(BD.getIndexofEtudiant("Charbel", "baloukji", Etudiant.cycleA))
    print(BD.getIndexofEtudiant("toni", "fares", Etudiant.cycleA))
    print(BD.editEtudiant("toni", "abifarah", Etudiant.cycleA, "Chahid", "khoury", Etudiant.cycleB))
    print(BD.containsEtudiant("ralph", "ahmad", Etudiant.cycleB))
    for etu in BD.etudiantList:
        print(etu)
    print("Finishing Test Etudiant!")

#Test Cours
def testCours():
    print("Test Cours!")
    BD.addCours("UTC503", "Paradigmes de Programmation", Cours.nivC)
    # print(*BD.etudiantList)
    print(BD.containsCours("UTC503", "Paradigmes de Programmation", Cours.nivC))
    print(BD.getIndexofCours("UTC503", "Paradigmes de Programmation", Cours.nivC))
    print(BD.getIndexofCours("UTC504", "Paradigmes de Programmation", Cours.nivC))
    print(BD.editCours("UTC503", "Paradigmes de Programmation", Cours.nivC, "Programmation Avancée", Cours.nivC))
    print(BD.containsCours("NFP121", "Programmation Avancée", Cours.nivC))
    for cours in BD.coursList:
        print(cours)
    print("Finishing Test Cours!")

def testNotes():
    print("Starting Test Notes!")

    print("Finishing Test Notes!")

testEtudiant()
testCours()
testNotes()