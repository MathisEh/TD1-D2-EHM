#! /usr/bin/env python3

"""Programme permettant de réaliser des opérations de chiffrement-déchiffrement par décalage
- Le texte à chiffrer ou déchiffrer sera fourni sur son l'entrée standard du programme.
- Lors de l'invocation du programme, l'utilisateur devra saisir lui-même le décalage à opérer, sous la forme d'un argument en ligne de commande. 
    - La classe `str` (dont héritent les chaînes de caractères dans un programme python) implémente la méthode `s.isnumeric` pour tester si une chaîne `s` est constituée exclusivement de caractères numériques. Malheureusement, cette méthode renvoie `False` lorsqu'elle est exécutée depuis la chaîne "-3"
    - Pour convertir une chaine de caractères numérique `s` en entier (on parle de *type casting*), on utilise la fonction `int(s)`. Cette fonction lève une exception si la conversion est impossible. 
    - 📌  Le **type casting** est l'opération qui consiste à convertir une valeur d'un type vers un autre type compatible, généralement en utilisant une opération ou une fonction de conversion.
- Si le programme est invoqué sans argument, il devra réaliser un chiffrement de César.
- Votre programme devra s'appuyer sur une fonction nommée `chiffrer` prenant deux arguments en paramètre : 
  - la chaîne à chiffrer. 
  - Le décalage (positif ou négatif) à opérer sur chacun des caractères alphabétiques de la chaine. 
- Les opérations de chiffrement-déchiffrement devront inverser la casse des caractères. Vous pourrez utiliser pour cela les *méthodes* `s.islower` et `s.isupper` de la classe `str`.  
- Votre programme devra traiter les caractères alphabétiques non accentués de manière générique en utilisant leurs codes ASCII.
- Votre programme devra traiter de manière spécifique les caractères accentués : il se contentera d'en changer la casse, sans réaliser de décalage.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

import sys

def traiterArguments():
  if len(sys.argv) <= 1:
    arg = 3
  else:
    arg = sys.argv[1]
    if (arg[0] == "-" and arg[1:].isnumeric() == False) or (arg[0] != "-" and arg.isnumeric() == False):
      print("l'argument n'est pas un entier")
      return 1

  return int(arg)

def lireStdin():
  s = sys.stdin.read()
  return s

def chiffrer(s,dec):
  s2 = ""
  accentMin = ["à", "â", "ä","é", "è", "ê", "ë","î", "ï","ô", "ö","ù", "û", "ü","ÿ","ç"]
  accentMaj = ["À", "Â", "Ä","É", "È", "Ê", "Ë","Î", "Ï","Ô", "Ö","Ù", "Û", "Ü","Ÿ","Ç"]
  for e in s:
    o = ord(e)
    if e in accentMin:
      indice = accentMin.index(e)
      s2 += accentMaj[indice]
    elif e in accentMaj:
      indice = accentMaj.index(e)
      s2 += accentMin[indice]
    elif o >= 97 and o <= 122:
      s2 += chr((o-32+dec) % 26 + 65)
    elif o >= 65 and o <= 90:
      s2 += chr((o+32+dec) % 26 + 97)
    else:
      s2 += e
  return s2

if __name__ == "__main__":
    dec = traiterArguments()
    s1 = lireStdin()
    print(chiffrer(s1,dec), end="")