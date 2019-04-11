#exercice portant sur le nombre de repetition
import random
nombre_secret = random.randint(0,9)
retour = none
retour = int(input("entrer une valeur comprise entre 0 et 9"
while True:
     if retour == nombre_secret:
       print("bravo,vous avez gagné")
     elif  retour > nombre_secret:
       print("le nombre_secret est inferieur au valeur donner")
     else:
       print("le nombre_secret est superieur au valeur donner")
     break
 
