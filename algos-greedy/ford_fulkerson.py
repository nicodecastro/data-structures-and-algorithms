# AUTHOR: John Nico T. De Castro
# CREATION DATE: 12/19/2024
# DESCRIPTION: A program that simulates the Ford-Fulkerson algorithm. Resource used: https://www.programiz.com/dsa/ford-fulkerson-algorithm.

INF = float('inf')

def dfs(source, sink, parent, graph):
    visited = [False] * len(graph)
    stack = []
    
    stack.append(source)
    visited[source] = True
    
    while stack:
        u = stack.pop()
        
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                stack.append(ind)
                visited[ind] = True
                parent[ind] = u
                
    return True if visited[sink] else False
    
    
    
def ford_fulkerson(source, sink, graph):
    parent = [-1] * len(graph)
    max_flow = 0
    
    while dfs(source, sink, parent, graph):
        
        path_flow = INF
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
            
        max_flow += path_flow
        
        v = sink
        while(v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
            
    return max_flow

def main():
    # Adjacency matrix of graph containing the capacities of each node
    graph = [
    #   S   A   B  C   D  T
        [0, 10, 0, 10, 0, 0],
        [0, 0, 4, 2, 8, 0],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 9, 0],
        [0, 0, 6, 0, 0, 10],
        [0, 0, 0, 0, 0, 0]
    ]
    
    # graph = [[0, 8, 0, 0, 3, 0],
    #      [0, 0, 9, 0, 0, 0],
    #      [0, 0, 0, 0, 7, 2],
    #      [0, 0, 0, 0, 0, 5],
    #      [0, 0, 7, 4, 0, 0],
    #      [0, 0, 0, 0, 0, 0]]
    
    source = 0
    sink = 5
    
    max_flow = ford_fulkerson(source, sink, graph)
    
    print(f"Max Flow: {max_flow}")
    
    
    
if __name__ == "__main__":
    main()