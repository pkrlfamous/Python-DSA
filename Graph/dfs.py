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

# def dfs(tree, node, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(node)

#     print(node, end=" ")

#     for child in tree[node]:
#         if child not in visited:
#             dfs(tree, child, visited)

# dfs(tree,'A',visited=None)


def dfs(tree, start):
    visited = set()
    stack = [start]



    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node , end = " ")
            stack.extend(reversed(tree[node]))

dfs(tree,'A')




