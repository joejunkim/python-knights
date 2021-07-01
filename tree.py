class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []


    @property
    def value(self):
        return self._value


    @property
    def children(self):
        return self._children


    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self


    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None


    @property
    def parent(self):
        return self._parent


    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = node
        if node:
            node.add_child(self)


    def __repr__(self):
        return f"Node({self.value})"


    # visited = set()
    # def depth_search(self, value, visited = set()):
    #     if value not in visited:
    #         visited.add(value)
    #         self.depth_search(value, visited)
    #     else:
    #         return None
    #     return self


    def depth_search(self, value, visited = set()):
        if self._value == value:
            return self
        if self not in visited:
            visited.add(self)
            for child in self._children:
                resultNode = child.depth_search(value, visited)
                if resultNode is not None:
                    return resultNode
        else:
            return None

node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)

 #self.parent = self.add_child(node)
#syntax-tactic sugar



# def dfs(visited, graph, node):
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

#dfs(visited, graph, 'A')
