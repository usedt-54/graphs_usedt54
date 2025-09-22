from graphs_usedt54 import sp
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Use: {sys.argv[0]} graph_file')
        sys.exit(1)

    graph = {}
    with open(sys.argv[1], 'rt') as f:
        f.readline()  # skip first line
        for line in f:
            s, d, w = map(int, line.strip().split())
            if s not in graph:
                graph[s] = {}
            graph[s][d] = w

    dist, path = sp.dijkstra(graph, 0)
    print(f"Shortest distances from 0: {dist}")
    for node in path:
        print(f"Path to {node}: {path[node]}")
