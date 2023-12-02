class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            cur_node = stack.pop()
            if cur_node not in visited:
                visited.add(cur_node)
                print(cur_node)

            for neighbor in self.adj_list[cur_node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Ejemplo de uso
adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph = Graph(adj_list)
graph.dfs('A')