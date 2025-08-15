import numpy as np

# Charger la Q-table sauvegardée
q_table = np.load("q_table.npy")

# Afficher la Q-table
print("Q-table actuelle :")
print(q_table)
