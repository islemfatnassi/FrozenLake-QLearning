import numpy as np

def save_q_table(q_table, filename="q_table.npy"):
    np.save(filename, q_table)
    print(f"Q-table saved to {filename}")

def load_q_table(filename="q_table.npy"):
    return np.load(filename)

def print_q_table(q_table):
    print("Q-table:")
    print(q_table)
