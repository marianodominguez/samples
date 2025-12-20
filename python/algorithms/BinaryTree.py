'''
Binary Tree

Binary Tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

Inorder: Left, Root, Right
Preorder: Root, Left, Right
Postorder: Left, Right, Root
BFS: Level Order
DFS: Preorder, Inorder, Postorder
Binary Search: Root, Left, Right
Height: Number of edges on the longest path from the root to a leaf

'''

from collections import deque

# Make a node safely for null values
def makeSafe(node):
    if node == None:
        return ""
    else:
        return node.content

# Node class
class Node:
    # Node constructor
    def __init__(self, x):
        self.content = x
        # Node left child
        self.left = None
        # Node right child
        self.right = None

    # Node string representation
    def __str__(self):
        return "/" + self.content + "/"

class Tree:
    # Tree constructor
    def __init__(self):
        # Tree root
        self.root = None

    # Add a node to the tree
    def add(self, node, pivot):
        if pivot == None:
            self.root = node
        else:
            if pivot.content < node.content:
                if pivot.right == None:
                    pivot.right = node
                else:
                    self.add(node, pivot.right)
            else:
                if pivot.left == None:
                    pivot.left = node
                else:
                    self.add(node, pivot.left)

    # put a node in the tree
    def put(self, x):
        n = Node(x)
        self.add(n, self.root)

    # Inorder traversal
    def inorder(self, node):
        if node == None:
            return []
        if node.left == None and node.right == None:
            return [node.content]
        else:
            result = []
            result.extend(self.inorder(node.left))
            result.extend([node.content])
            result.extend(self.inorder(node.right))
            return result

    # Postorder traversal
    def postorder(self, node):
        if node == None:
            return []
        if node.left == None and node.right == None:
            return [node.content]
        else:
            result = []
            result.extend(self.postorder(node.left))
            result.extend(self.postorder(node.right))
            result.extend([node.content])
            return result

    # Preorder traversal
    def preorder(self, node):
        if node == None:
            return []
        if node.left == None and node.right == None:
            return [node.content]
        else:
            result = []
            result.extend([node.content])
            result.extend(self.preorder(node.left))
            result.extend(self.preorder(node.right))
            return result

    # Breadth First Search
    def bfs(self, nodeToSearch):
        visited = []
        queue = deque([self.root])
        current = self.root
        path = []

        while True:
            if queue == []:
                return []
            if current.content == nodeToSearch:
                return [(x.content, makeSafe(x.left), makeSafe(x.right)) for x in path]

            if current not in visited:
                for next in [current.left, current.right]:
                    if next != None:
                        queue.append(next)
                visited.append(current)
            current = queue.popleft()
            path.append(current)

    # Depth First Search
    def dfs(self, nodeToSearch):
        visited = []
        stack = [self.root]
        current = self.root
        path = []

        while True:
            if stack == []:
                return []
            if current.content == nodeToSearch:
                return [(x.content, makeSafe(x.left), makeSafe(x.right)) for x in path]
            if current not in visited:
                for next in [current.left, current.right]:
                    if next != None:
                        stack.append(next)
                visited.append(current)
            current = stack.pop()
            path.append(current)

    # Binary Search
    def binarySearch(self, nodeToSearch):
        current = self.root
        path = [self.root]
        while True:
            if current.content == nodeToSearch:
                return [(x.content, makeSafe(x.left), makeSafe(x.right)) for x in path]
            next = None
            if nodeToSearch < current.content:
                if current.left != None:
                    next = current.left
            else:
                if current.right != None:
                    next = current.right
            if next == None:
                return []
            path.append(next)
            current = next
    
    # Height of the tree
    def height(self, root):
        stack=[[root]]
        path=[]
        visited=[]
        maxlen=1
        while stack:
            path=stack.pop()
            current=path[-1]
            visited.append(current)
            if current.right and current.right not in visited:
                newpath=path.copy()
                newpath.append(current.right)
                stack.append(newpath)
            if current.left and current.left not in visited:
                newpath=path.copy()
                newpath.append(current.left)
                stack.append(newpath)
            if len(path)>maxlen: maxlen=len(path)
        return maxlen