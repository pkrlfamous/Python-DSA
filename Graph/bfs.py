# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],  # Node A connects to B and C
    'B': ['A','D', 'E'],  # Node B connects to A, D and E
    'C': ['F', 'G'],  # Node C connects to F and G
    'D': ['H', 'I'],  # Node D connects to H and I
    'E': ['J', 'K'],  # Node E connects to J and K
    'F': ['L', 'M'],  # Node F connects to L and M
    'G': ['N', 'O'],  # Node G connects to N and O
    'H': [], 'I': [], 'J': [], 'K': [],  # Leaf nodes have no children
    'L': [], 'M': [], 'N': [], 'O': []   # Leaf nodes have no children
}


# def bfs(tree, start):
#     visited = {start}
#     queue = [start]

#     while queue:
#         node = queue.pop(0)
#         print(node, end=" ")
#         for neighbors in tree[node]:
#             if neighbors not in visited:
#                 queue.append(neighbors)
#                 visited.add(neighbors)
#     print(visited)

# bfs(tree, 'A')

# def bfs(tree, start):
#     visited = []
#     queue = [start]

#     while queue:
#         node = queue.pop(0)
#         print(node, end=" ")
#         visited.append(node)

#         for neighbors in tree[node]:
#             if neighbors not in visited:
#                 queue.append(neighbors)

#     print(visited)
# bfs(tree, 'A')

from collections import deque

def bfs(tree,start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)
        print(node, end=" ")

        for neighbor in tree[node]:
            if neighbor not in visited:
                queue.append(neighbor)
        
    
bfs(tree, 'A')