import gymnasium as gym
import numpy as np
import time

# Charger la Q-table
q_table = np.load("q_table.npy")

# Créer l'environnement avec render_mode='human'
env = gym.make("FrozenLake-v1", is_slippery=True, render_mode="human")

num_episodes = 5

for episode in range(num_episodes):
    state, _ = env.reset()
    done = False
    total_reward = 0
    print(f"Episode {episode + 1}:")

    while not done:
        # Choisir la meilleure action
        action = np.argmax(q_table[state])
        state, reward, done, truncated, info = env.step(action)
        total_reward += reward
        time.sleep(0.5)  # Pour voir l’agent se déplacer

    print(f"Récompense obtenue : {total_reward}\n")

env.close()
