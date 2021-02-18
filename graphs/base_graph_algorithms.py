from typing import Dict
from collections import deque, defaultdict

class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False

def bfs(root: int, nodes: Dict[int, Node], adj_dict: Dict[int, int]):
    queue = deque()
    queue.append(root)
    nodes[root].visited = True
    
    while queue:
        cur_vertex = queue.popleft()
        for neighbour_id in adj_dict.get(cur_vertex, []):
            neighbour_node = nodes[neighbour_id]
            if not neighbour_node.visited:
                print(neighbour_id)
                queue.append(neighbour_id)
                neighbour_node.visited = True

def recursive_dfs(cur_vertex_id: int, nodes: Dict[int, Node], adj_dict: Dict[int, int]):
    print(cur_vertex_id)
    nodes[cur_vertex_id].visited = True
    
    for neighbour_id in adj_dict.get(cur_vertex_id, []):
        if not nodes[neighbour_id].visited:
            recursive_dfs(neighbour_id, nodes, adj_dict)
    

def dfs(root: int, nodes: Dict[int, Node], adj_dict: Dict[int, int]):
    stack = [root]
    
    while stack:
        cur_vertex_id = stack.pop()
        if nodes[cur_vertex_id].visited:
            continue
        
        print(cur_vertex_id)
        nodes[cur_vertex_id].visited = True
        
        for neighbour_id in reversed(adj_dict.get(cur_vertex_id, [])):
            stack.append(neighbour_id)    
    
    

if __name__ == "__main__":
    nodes_count = 13
    paths = [[0, 1], [0, 2], [0, 3], [1, 4], [4,5], [2, 6], [6, 7], [6, 8], [8, 9], [8, 10], [1, 11], [1, 12]]
    nodes = {i: Node(i) for i in range(nodes_count)}
    adj_dict = defaultdict(list)
    for node_i, node_j in paths:
        adj_dict[node_i].append(node_j)
    recursive_dfs(0, nodes=nodes, adj_dict=adj_dict)
    