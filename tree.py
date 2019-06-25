import collections
import math

si = []

def breadth_first_search(graph, root): 
    visited, queue = set(), collections.deque([root])
    while queue: 
        vertex = queue.popleft()
        visit(vertex)
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 



def visit(n):
    print(n)

def bread_first_s(array, goal):
    j = math.trunc(len(array)/2 )


    print(j)
    print(len(array))
    
 
def dfs(self, node):
    visited = [False for i in range(len(self.graph))]
    stack = []
    stack.append(node)
    while stack:
        node = stack.pop()
        if not visited[node]:
            print(node)
            visited[node] = True
            for i in self.graph[node]:
                stack.append(i)


def left(i):
    return 2 * i
def right(i):
    return 2 * i + 1
if __name__ == '__main__':
    #graph = {0: [1, 2], 1: [2], 2: []} 
    graph = {
    'J' : ['A','N'],
    'A' : ['U','L'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
    }
    array = ['J','A','N','U','L','R','Y','Z','V','H','T','F','R','D','C']
    goal = 'H'

    #bread_first_s(array,goal)
     
    breadth_first_search(graph, 'J')
