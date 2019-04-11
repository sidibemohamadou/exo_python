#variable aleatoire
import random
nombre_secret = random.randint(0,9)
answer = none
do{ answer = int(input("entrer une valeur comprise entre 0 et 9")
                 }
while answer != nombre_secret :
     
     if  answer > nombre_secret :
       print("le nombre_secret est inferieur au valeur donner")
     elif answer < nombre_secret :
       print("le nombre_secret est superieur au valeur donner")
     else:
       print("bravo,vous avez gagné")
 
