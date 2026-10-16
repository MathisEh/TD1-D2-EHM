#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques détaillées. 
- ***Cet exercice s'inspire largement d'un TP construit par Christian Vercauter, enseignant d'informatique à l'Ecole Centrale de Lille, aujoud'hui retraité.***
- Le programme doit afficher en plus des informations précédentes du programme comptage : 
    - Le nombre total de caractères alphabétiques rencontrés. 
    - Un tableau présentant le nombre d'occurrences de chaque caractère alphabétique, ainsi que sa fréquence (rapport entre le nombre d'occurrences d'un caractère alphabétique sur le nombre total de caractères alphabétiques).
- **Indications** : Créer et initialiser à zéro, une liste de 29 composantes entières, qui contiendra les occurrences des caractères alphabétiques mais également le nombre total de mots, lignes, caractères et caractères alphabétiques rencontrés. 
- Considérer les caractères accentués de manière spéficique à l'aide d'un `match/case`; 
- Tester votre programme sur les deux extraits du roman de Georges Perec (1936-1982) intitulé "La Disparition" paru en 1969. Que remarquez-vous en examinant les résultats ?
- Tester votre programme sur l'extrait d'un autre roman de Georges Perec, intitulé "Les Revenentes" paru en 1972. Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **lipogramme** ?
- Tester votre programme sur le texte suivant : *"Portez ce vieux whisky au juge blond qui fume"*. Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **pangramme** ? A quoi servent les pangrammes en informatique ?
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 
"""
import sys
import comptage
def lire():
    chemin = sys.argv[1]
    try:
        flux = open(chemin,'r')
        s = flux.read()
    except:
        print("erreur, le fichier n'existe pas")
        return 1
    if s == "":
        print("fichier vide")
        return 0
    compt = [0 for i in range(0,26)]
    for i in range(0,len(s)):
        match s[i]:
            case "é":
                compt[4] += 1
            case "è":
                compt[4] += 1
            case "ê":
                compt[4] += 1
            case "à":
                compt[0] += 1
            case "ç":
                compt[2] += 1
            case _ :
                o = ord(s[i])
                if o >= 65 and o <= 90:
                    compt[o-65] += 1
                if o >= 97 and o <= 122:
                    compt[o-97] += 1
    tot = 0
    for e in compt:
        tot = e + tot
    l = comptage.lire(chemin)

    for i in range(0,26):
        print(chr(i+97),"|",compt[i],"|",compt[i]/tot*100,"%")
    return 0


if __name__ == "__main__":
    lire()
