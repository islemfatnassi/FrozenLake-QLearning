from q_learning import QLearningAgent
from utils import save_q_table

if __name__ == "__main__":
    agent = QLearningAgent()
    print("Début de l'entraînement...")
    rewards = agent.train()
    print(f"Score moyen : {sum(rewards)/len(rewards):.3f}")
    save_q_table(agent.get_q_table())
