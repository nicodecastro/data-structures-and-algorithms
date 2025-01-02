# AUTHOR: John Nico T. De Castro
# CREATION DATE: 12/24/2024
# DESCRIPTION: A program that finds hamiltonian paths.

def hamiltonian(graph, x, k):
    n = len(graph)
    
    while True:
        next_vertex(graph, x, k)
        if x[k] == 0:
            break
        if k == n-1:
            print(x)
        else:
            hamiltonian(graph, x, k + 1)
            
def next_vertex(graph, x, k):
    n = len(graph)
    
    while True:
        x[k] = (x[k] + 1) % (n + 1)
        if x[k] == 0 or k == 0:
            return
        if graph[x[k - 1]-1][x[k]-1] != 0:      # check for edge between prev & cur node
            for i in range(k+1):
                if x[i] == x[k]:
                    break
            if i == k:
                if k < n or (k == n and graph[x[n]-1][x[0]-1] != 0):
                    return
                
        

def main():
    graph = [
    #    # 0  1  2  3
    #     [0, 1, 0, 0],   # 0
    #     [1, 0, 1, 1],   # 1
    #     [0, 1, 0, 1],   # 2
    #     [0, 1, 1, 0]    # 3
            # [0, 1, 0, 0],
            # [1, 0, 1, 1],
            # [0, 1, 0, 0],
            # [0, 1, 0, 0]
        [0,1,1,0,1],
        [1,0,1,1,1],
        [1,1,0,1,0],
        [0,1,1,0,1],
        [1,1,0,1,0]
    ]
    x = [0] * len(graph)
    hamiltonian(graph, x, 0)

if __name__ == "__main__":
    main()