# le Binaire est le système de nombre utilisé par tous les ordinateurs => Important de comprendre le Binaire
# but de Bin2Dec => pratiquer & comprendre comment fonctionne les calcules binaires 

# Bin2Dec permet :
#   - à l'utilisateur d'entrer un string de 8 chiffre binaires => des 0 & des 1 
#   - dans nimporte quel ordre
#   - et Affiche son équivalent décimal

# 2 contraintes : 
#   - Tableaux ne peuvent pas être utilisés pour contenir les chiffres binaires entrés par l'utilisateur
#   - Déterminer le nombre décimal équivalent d'un nombre binaire particulier dans la séquence doit être calculé en utilisant une seule fonction
#       mathématique (ex : Le logarithme naturel) => A moi de décider quelle fonction utiliser

# 1) Utilisateur peut entrer 8 chiffres binaires dans un champs d'entrée
# 2) Utilisateur doit être notifié s'il rentre autre chose que des 0 & des 1
# 3) Utilisateur voit le résultat dans un seul champs de sortie content le décimal (base 10) équivalent au nombre binaire qui a été entré
# 4) Utilisateur peut entrer un nombre variable de chiffre binaire

# Le système numérique de base-2 est une notation positionnelle avec un radix de 2. Chaque chiffre est appelé un bit, ou chiffre binaire.
# 1 = 1, 2 = 10, 4 = 2*2 = 10 * 10 = 100, 8 = 2 * 4 = 100 * 100 = 1 000, 16 = 2 * 8 = 1 000 * 1 000 = 10 000
# La signification des représentation dépend de la base utilisé => 2 en base deux
# On utilise 0 & 1
# 1101 en base 2 => 1 * 2 puissance 3 + 1 * 2 puissance 2 + 0 * 2 puissance 1 + 1 * 2 puissance 0 = 13
# On donne à chaque bit une puissance de deux, comme cette suite 1, 2, 4, 8, 16, 32, 64. Pour obtenir le nombre 7, 
# on additionne les trois premiers bits; pour obtenir 6, on additionne seulement le bit de poids 4 et le bit de poids 2.


def verifier_input(input):
    for i in binary_numbers:
        if not i.isdigit():
            print("Erreur : Pas un chiffre. Problème :", i)
            return 
        if i != "0" and i != "1":
            print("Uniquement des 0 & des 1. Problème :", i)
            return 
    
    return True
        


binary_numbers = input("Veuillez entrer un nombre binaire, composé de 0 et de 1, d'une taille de 8 chiffres : ")

while len(binary_numbers) != 8:
    print("Entrez 8 chiffres")
    binary_numbers = input("Veuillez entrer un nombre binaire, composé de 0 et de 1, d'une taille de 8 chiffres : ")

if verifier_input(binary_numbers):
    #binaire = "0b" + binary_numbers
    print(int(binary_numbers, 2))
    print(bin(255))


            
    
