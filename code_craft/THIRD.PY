# Depth-First Search (DFS) implementation using adjacency list

def dfs(graph, vertex, visited):
    
    visited.add(vertex)
    print(vertex, end=" ")  
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    visited = set()
    
    print("DFS Traversal starting from vertex A:")
    dfs(graph, 'A', visited)
