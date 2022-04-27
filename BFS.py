def bfs(graph, node, goal):
    visited, queue = [], []
    visited.append(node), queue.append(node)

    while queue:
        m = queue.pop(0)
        cost = 1
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                cost = cost +1
                if neighbour == goal:

                    return visited

    return 'Item not in List'







graph = {
    '1': ['8', '5', '2'],
    '8': ['6', '4', '3'],
    '5': [],
    '2': ['9'],
    '6': ['10', '7'],
    '4': [],
    '3' :[]
}




print("Breadth First Search")
start = input("Enter start node: ")
goal = input("Enter goal node: ")
print(bfs(graph, start, goal))

