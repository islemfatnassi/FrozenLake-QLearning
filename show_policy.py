import numpy as np

# Charger la Q-table
q_table = np.load("q_table.npy")

# Définir les actions
actions = ['←', '↓', '→', '↑']  # gauche, bas, droite, haut

print("Politique optimale par état :")
for state in range(q_table.shape[0]):
    best_action = actions[np.argmax(q_table[state])]
    print(f"État {state} -> {best_action}")
