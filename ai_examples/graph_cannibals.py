from itertools import product
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Define total missionaries and cannibals
TOTAL_M = 3
TOTAL_C = 3

# Possible raft moves (M, C): 1 or 2 people total
POSSIBLE_MOVES = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

# Helper to convert state to string for labeling
def state_str(ML, CL, raft):
    MR = 3 - ML
    CR = 3 - CL
    if raft == 'L':
        return f"{''.join(['M']*ML + ['C']*CL)}R|{''.join(['M']*MR + ['C']*CR)}"
    else:
        return f"{''.join(['M']*ML + ['C']*CL)}|R{''.join(['M']*MR + ['C']*CR)}"


# Check if a state is valid
def is_valid_state(ML, CL):
    MR = TOTAL_M - ML
    CR = TOTAL_C - CL
    if ML < 0 or CL < 0 or MR < 0 or CR < 0:
        return False
    if (ML > 0 and CL > ML) or (MR > 0 and CR > MR):
        return False
    return True

# Generate all valid transitions
def generate_valid_transitions():
    G = nx.DiGraph()
    visited = set()
    queue = deque([ (3, 3, 'L') ])  # (ML, CL, raft)

    while queue:
        ML, CL, raft = queue.popleft()
        current_state = (ML, CL, raft)
        visited.add(current_state)

        for m, c in POSSIBLE_MOVES:
            if raft == 'L':
                new_ML = ML - m
                new_CL = CL - c
                new_raft = 'R'
            else:
                new_ML = ML + m
                new_CL = CL + c
                new_raft = 'L'

            new_state = (new_ML, new_CL, new_raft)

            if is_valid_state(new_ML, new_CL):
                if new_state not in visited:
                    queue.append(new_state)

                # Add edge with labels
                src = state_str(ML, CL, raft)
                dst = state_str(new_ML, new_CL, new_raft)
                G.add_edge(src, dst)

    return G

# Generate graph
G_all = generate_valid_transitions()

# Draw the graph
plt.figure(figsize=(24, 18))
pos = nx.spring_layout(G_all, seed=1)
nx.draw(G_all, pos, with_labels=True, node_size=3000, node_color="lightyellow", font_size=16, font_family="monospace", arrowsize=16)
plt.title("All Valid Movements: Missionaries and Cannibals")
plt.show()
