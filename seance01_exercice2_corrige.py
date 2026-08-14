"""
Séance 1 — Exercice 2 : Rappel — boucles (CORRIGÉ)
"""

n = 10
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print(total)   # attendu : 30
