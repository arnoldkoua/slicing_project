######################## exo 1 ############################""

"""dans cette exercise vous devez rÃ©cuperer les diffÃ©rents morceaux
de la liste grace aux slices

la de dÃ©part est la suivante

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
L'objectif de cet exercise est de rÃ©cuperer les informations grace aux slices:

--Les trois premiers employÃ©s ('Maxime', "Martine", "Christopher") dans une liste
trois premiers

--les trois derniers employÃ©s ('Carlos', "Michael" et Eric) dans une liste les trois
derniers.

--tous les employÃ©s sauf le premiers et le derniers dans une liste milieu

--Le premier et le derniers employÃ©dans une liste premier_dernier

"""

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[:3]
trois_derniers = liste[-3:]
milieu = liste[2:4]
premier_dernier = [liste[0], liste[-1]]

################################ exo 2 #######################################

"""
Dans cet exercice, vous devez  ajouter le nombre 6 dans la liste.
Faites une vÃ©rification par la suite pour vous assurer que l'Ã©lÃ©ment a bien Ã©tÃ© ajoutÃ©.

La liste de dÃ©part est la suivante :
liste = [1, 2, 3, 4, 5] Vous devez ajouter le nombre 6 dans la liste.
VÃ©rifiez ensuite si le nombre 6 est prÃ©sent dans la liste, si c'est le cas, 
affichez la chaÃ®ne de caractÃ¨res  Le nombre 6 a bien Ã©tÃ© ajoutÃ© Ã  la liste.
"""
liste = [1, 2, 3, 4, 5]
liste.append(6)

if liste.count(6) > 0:
    print("Le nombre 6 a bien été ajouté à la liste.")

################################ exo 3 #######################################

"""
RÃ©cupÃ©rer des Ã©lÃ©ments dans une liste imbriquÃ©e
Dans cet exercice, vous devez rÃ©cupÃ©rer des informations Ã  l'intÃ©rieur de deux  listes imbriquÃ©es.
Le script dispose de deux listes contenant plusieurs listes imbriquÃ©es, une liste langage et une liste nombres. 
Vous devez rÃ©cupÃ©rer dans les variables python, deux et sept, respectivement la chaÃ®ne de caractÃ¨res 'Python'
 contenue dans la liste langages et les nombres 2 et 7, contenus dans la liste nombres.
Vous n'avez pas besoin d'afficher les variables avec print, 
il suffit de rÃ©cupÃ©rer les bonnes valeurs dans les variables Ã  partir 
des listes et avec les indices des Ã©lÃ©ments.


"""

langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

python = langages[0][0]
deux = nombres[1][1][0]
sept = nombres[4][0][0]