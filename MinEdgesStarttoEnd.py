### Given an integer n that represents the number of vertices, labeled from 0 to n-1, 
### an array edges of undirected edges, a vertex start and a vertex end, 
### we want to find the minimum number of edges to go from start to end.


def min_edges(n, edges, start, end):
    graph = [[] for _ in range(n)]
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    queue = Queue()
    visited = set()
    queue.put((start, 0))
    visited.add(start)
    while not queue.empty():
        vertex, level = queue.get()
        if vertex == end:
            return level
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.put((neighbor, level + 1))
                visited.add(neighbor)
    return -1