print("\nBonjour Mesdames et Monsieur dans ce Motus diffusé sur Programme 3")

print("\nLes règles sont très simple, le jeu choisira au hasard 1 mot parmis tant d'autre")

print("\nSi la lettre correspond au mot chercher celle-ci s'affichera en rouge")

print("\nPar contre si celle-ci ne correspond pas au mot rechercher celle-ci s'affichera en bleu")

print("\nPour finir si vous avez taper une lettre qui se met en jaune c'est que celle-ci est bien dans le mot que l'on cherche mais elle n'est pas à la bonne place !")
print("\nLe mot que vous allez deviner est le suivant")
import random
choix = ["brindille", "constituer", "silence", "raton", "chaton", "biberon", "douche", "hippopotomonstroléquipédialophobie", "obliger", "permission"]
solution = random.choice(choix)

solution = random.choice(choix)
tentatives = 10

affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

while tentatives > 0:
  print("\nLettre à proposer : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> C'est effectivement la lettre que nous cherchons")

  else:
    tentatives = tentatives - 1
    print("-> Ce n'est pas la bonne lettre que nous cherchons\n")

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Bien jouer ! Vous êtes maintenant le champion de notre jeu Motus ! Félicitations ! <<<")
      break

if "_" in affichage:
      print("    Dommage tu n'as pas pu trouver le mot tu retentera une prochaine fois ! <<<")
      

print("\n     C'est la fin de notre jeu Téléviser   ")

print("\n    Veut-tu retenter notre jeux ?    ")
print("\nSi oui tu as juste à appuyer sur la petite croix puis faire Ctrl+F5, et si tu as appuyer directement sur le fichier tu peut le fermer et recommencer ! A tout de suite !")
print("\nSi tu ne veux pas ce n'est pas grave tu pourra toujours recommencer une prochaine fois !")
print("\n           A la prochaine pour tenter de gagner notre jeux Motus")