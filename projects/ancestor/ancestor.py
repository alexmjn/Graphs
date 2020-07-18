# plan
## graphs problem solving
## translate problem, nodes people
# edges when child has a parent

# build or graph? or just define get_neighbors?

## choose algorithm - dfs (we want to build thing)

## how would we know what's faster?

# import deque from collections

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

graph = Graph()

def build_graph(ancestors):
    for parent, child in ancestors:

        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(parent, child)

    return graph

def earliest_ancestor2(ancestors, starting_node):
    graph = build_graph(ancestors)

    s = Stack()
    visited = set()
    s.push([starting_node])
    longest_path = []
    aged_one = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)
            parents = graph.get_neighbors(current_node)
            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)

    return longest_path[-1]

def earliest_ancestor(ancestors, starting_node):
    adjacency_list = {}
    for parent, child in ancestors:
        if child not in adjacency_list:
            adjacency_list[child] = {parent}
        else:
            adjacency_list[child] = adjacency_list[child].union({parent})

    s = [starting_node]
    preds = {}
    generations = 0
    preds[generations] = []

    while len(s) > 0:
        earliest = s.pop()
        if len(s) == 0:
            new_gen = True
        else:
            new_gen = False

        if earliest in adjacency_list:
            for ancestor in adjacency_list[earliest]:
                s.append(ancestor)
        else:
            preds[generations].append(earliest)
        if new_gen:
            generations += 1
            preds[generations] = []

    if earliest == starting_node:
        return -1
    else:
        target = preds[generations-1]
        if len(target) > 1:
            return min(target)
        return target.pop()
