import gymnasium as gym
from q_learning import QLearningAgent
from utils import load_q_table
import time
from config import TEST_EPISODES, MAX_STEPS

if __name__ == "__main__":
    agent = QLearningAgent()
    agent.q_table = load_q_table()  # Charger la Q-table entraînée
    env = agent.env

    for episode in range(TEST_EPISODES):
        state, _ = env.reset()
        print(f"\nÉpisode {episode+1}")
        time.sleep(1)
        for step in range(MAX_STEPS):
            print(env.render())  # Affichage texte
            action = int(agent.q_table[state, :].argmax())
            new_state, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            state = new_state
            time.sleep(0.5)
            if done:
                if reward == 1:
                    print("Agent a atteint le but ! ")
                else:
                    print("Agent est tombé dans un trou ")
                break
    env.close()
