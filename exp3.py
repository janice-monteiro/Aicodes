#graph = {
#  'A' : ['B','C','D'],
#  'B' : ['E', 'F'],
#  'C' : ['F'],
#  'D' : [],
#  'E' : [],
 # 'F' : []
#}
graph = {
    '1': ['8', '5', '2'],
    '8': ['6', '4', '3'],
    '5': [],
    '2': ['9'],
    '6': ['10', '7'],
    '4': [],
    '3' :[],
    '9' :[],
    '10':[],
    '7' :[]
}

def bfs(graph, root, goal):
    queue = []
    closed = []
    opened =[]
    path = 0
    queue.append(root)
    opened.append(root)
    #key should be spilt and added to queue
    liist = graph[root] # <- nodes connected to root node in form of list
    for element in liist:
        queue.append(element)#<- storing nodes in queue individually n not as list
        opened.append(element)
    closed.append(opened.pop(0))
    path = path + 1
    while (goal not in closed):
        list1 = graph[opened[0]]
        for node in list1:
            if(node not in queue):
                queue.append(node)
                opened.append(node)
        closed.append(opened.pop(0))
        path += 1
        
    final_bfs = ''.join([str(node) for node in closed])
    print('BFS: ' + str(final_bfs))
    print('Cost: ', path)          

def dfs(graph, root, goal):
    stack = []
    opened=[]
    closed = []
    path = 0
    stack.append(root)
    opened.append(root)
    path =+ 1
    #key should be spilt and added to queue in a reverse order alphabetical
    liist = graph[root] # <- nodes connected to root node in form of list
    closed.append(opened.pop())
    for element in reversed(liist):
        stack.append(element)#<- storing nodes in queue individually n not as list
        opened.append(element)
    while (goal not in closed):
        list1 = graph[opened[-1]]
        closed.append(opened.pop())
        path += 1
        for node in reversed(list1):
            if(node not in stack):
                stack.append(node)
                opened.append(node)
        
    final_dfs = ''.join([str(node) for node in closed])
    print('DFS: ' + str(final_dfs))
    print('Cost: ', path)
    

print("Input graph: "+ str(graph))
root = input("Enter initial node: ")
goal = input("Enter goal node: ")
bfs(graph, root, goal)
dfs(graph, root, goal)
