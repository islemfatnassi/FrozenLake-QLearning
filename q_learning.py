import gymnasium as gym
import numpy as np
import random
from config import *

class QLearningAgent:
    def __init__(self):
        self.env = gym.make(ENV_NAME, is_slippery=IS_SLIPPERY)
        self.state_size = self.env.observation_space.n
        self.action_size = self.env.action_space.n
        self.q_table = np.zeros((self.state_size, self.action_size))

    def train(self):
        epsilon = EPSILON
        rewards = []

        for episode in range(TOTAL_EPISODES):
            state, _ = self.env.reset()
            total_rewards = 0

            for step in range(MAX_STEPS):
                # Exploration-exploitation
                if random.uniform(0, 1) < epsilon:
                    action = self.env.action_space.sample()
                else:
                    action = np.argmax(self.q_table[state, :])

                new_state, reward, terminated, truncated, info = self.env.step(action)
                done = terminated or truncated

                # Q-Learning update
                self.q_table[state, action] = self.q_table[state, action] + LEARNING_RATE * (
                    reward + GAMMA * np.max(self.q_table[new_state, :]) - self.q_table[state, action]
                )

                total_rewards += reward
                state = new_state
                if done:
                    break

            # Décroissance epsilon
            epsilon = MIN_EPSILON + (MAX_EPSILON - MIN_EPSILON) * np.exp(-DECAY_RATE*episode)
            rewards.append(total_rewards)

        return rewards

    def get_q_table(self):
        return self.q_table
