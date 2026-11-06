from random import choice
from itertools import permutations
import os

participants = ['Anne', 'Benjamin', 'Elsa', 'Eric', 'Maria', 'Nicolas', 'Pierre', 'Sarah', 'Laure', 'Samy']
n = len(participants)

couples = {('Anne', 'Benjamin'),
           ('Elsa', 'Nicolas'),
           ('Eric', 'Maria'),
           ('Pierre', 'Sarah'),
           ('Laure', 'Samy')}

_, annee = os.getcwd().split("noel_")

an_dernier = set()
for nom in participants:
    try:
        with open(f'../noel_{int(annee) - 1}/{nom}.txt') as fichier:
            a, *_, b = [*fichier][0].split()
            an_dernier.add((a, b))
    except:
        ...
print(an_dernier)

perm = [p for p in permutations(participants)
        if all((*sorted((p[k-1], p[k])),) not in couples for k in range(n))]
print("boucles sans couples :", len(perm))
perm = [p for p in perm
        if all((p[k-1], p[k]) not in an_dernier for k in range(n))]
print("boucles sans couples et differentes de l'an dernier :", len(perm))

p = choice(perm)

for k in range(n):
    a, b = p[k-1], p[k]
    with open(f'{a}.txt', 'w') as fichier:
        fichier.write(f'{a} offre un cadeau a {b}')

input()