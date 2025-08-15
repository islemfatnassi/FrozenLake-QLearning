# Environment
ENV_NAME = "FrozenLake-v1"
IS_SLIPPERY = True

# Q-Learning Hyperparameters
TOTAL_EPISODES = 10000       # Nombre d'épisodes pour un meilleur apprentissage
MAX_STEPS = 100
LEARNING_RATE = 0.8
GAMMA = 0.95

# Exploration parameters
EPSILON = 1.0
MAX_EPSILON = 1.0
MIN_EPSILON = 0.01
DECAY_RATE = 0.005

# Testing
TEST_EPISODES = 10
