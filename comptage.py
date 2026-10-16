#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques principales.
- Le chemin du fichier à lire devra être fourni comme argument en ligne de commandes. 
- En absence d'argument, le programme lira les caractères fournis sur l'entrée standard. 
- Le programme doit afficher le nombre de caractères, de lignes et de mots du texte lu. Pour cela, vous devez utiliser la structure de contrôle match/case afin de discrimer la nature des caractères au fur et à mesure de leur lecture. 
- De façon à ne pas trop compliquer les traitements, on considérera qu'un mot est une séquence de caractères encadrée de séparateurs et dans un premier temps, seuls trois séparateurs seront pris en compte : le saut de ligne, l'espace et le caractère de tabulation ('\t')
- Votre programme devra proposer un mode de débogage affichant les numéros des mots détectés. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""
import sys,os

def lire():
    if len(sys.argv)>1:
        chemin = sys.argv[1]
        try:
            flux = open(chemin,'r')
            s = flux.read()
        except:
            print("erreur, le fichier n'existe pas")
            return 1
    else:
        s = sys.stdin.read()
    nbrchar = 0
    nbrmots = 0
    nbrligne = 0
    for i in range(0,len(s)):
        if s[i] == "\n":
            nbrligne += 1
            nbrmots += 1
        elif (s[i] == " " or s[i] == "\t") and (s[i+1] != "\n"):
            nbrmots += 1
        nbrchar += 1
    if s[-1] != "\n" and s[-1] != "\t" and s[-1] != " ":
        nbrligne += 1
        nbrmots += 1                   #on considère "\n", "\t", " " comme des caractère
    print("nombre de lettre:", nbrchar)
    print("nombre de mots:", nbrmots)
    print("nombre de ligne:", nbrligne)
    return 0

    



    
    


if __name__ == "__main__":
    lire()
