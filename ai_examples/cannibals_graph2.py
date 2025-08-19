import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# Initialize the graph
G = nx.DiGraph()

# Start from the initial state: 3 missionaries, 3 cannibals on the left, raft on the left
initial_state = (3, 3, 'L')
G.add_node(initial_state)

# Queue for BFS traversal
queue = deque([initial_state])
visited = set()
visited.add(initial_state)

# BFS to build the graph
while queue:
    current_state = queue.popleft()
    M_left, C_left, raft_side = current_state

    if raft_side == 'L':
        # Move from left to right
        for move_count in [1, 2]:
            for m in range(0, move_count + 1):
                c = move_count - m
                if m > M_left or c > C_left:
                    continue
                new_M_left = M_left - m
                new_C_left = C_left - c
                new_M_right = 3 - new_M_left
                new_C_right = 3 - new_C_left
                valid_left = (new_M_left >= new_C_left) or (new_C_left == 0)
                valid_right = (new_M_right >= new_C_right) or (new_C_right == 0)
                if valid_left and valid_right:
                    new_raft_side = 'R'
                    new_state = (new_M_left, new_C_left, new_raft_side)
                    if new_state not in visited:
                        G.add_node(new_state)
                        G.add_edge(current_state, new_state)
                        visited.add(new_state)
                        queue.append(new_state)
    else:
        # Move from right to left
        M_right = 3 - M_left
        C_right = 3 - C_left
        for move_count in [1, 2]:
            for m in range(0, move_count + 1):
                c = move_count - m
                if m > M_right or c > C_right:
                    continue
                new_M_left = M_left + m
                new_C_left = C_left + c
                new_M_right = 3 - new_M_left
                new_C_right = 3 - new_C_left
                valid_left = (new_M_left >= new_C_left) or (new_C_left == 0)
                valid_right = (new_M_right >= new_C_right) or (new_C_right == 0)
                if valid_left and valid_right:
                    new_raft_side = 'L'
                    new_state = (new_M_left, new_C_left, new_raft_side)
                    if new_state not in visited:
                        G.add_node(new_state)
                        G.add_edge(current_state, new_state)
                        visited.add(new_state)
                        queue.append(new_state)

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=False, node_size=2000)
labels = {node: str(node) for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels)
plt.show()