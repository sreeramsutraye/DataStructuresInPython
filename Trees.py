class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)
class Stack(object):
    def __init__(self):
        self.stck = []
    def push(self,key):
        self.stck.append(key)
    def pop(self):
        return self.stck.pop()
    def __len__(self):
        return len(self.stck)
    def topofthestack(self):
        return self.stck[-1]
    def is_empty(self):
        if len(self.stck) == 0:
            return True
        else:
            return False 
class Tree(object):
    def __init__(self,root):
        self.root = Node(root)
    def printing_tree(self,typeoforder):
        traversal = ""
        if typeoforder == "preorder":
            return self.preorder_traversal(self.root,traversal)
        if typeoforder == "inorder":
            return self.inorder_traversal(self.root,traversal)
        if typeoforder == "postorder":
            return self.postorder_traversal(self.root,traversal)
        else:
            return
    def preorder_traversal(self,start,traversal):
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.preorder_traversal(start.left,traversal)
            traversal = self.preorder_traversal(start.right,traversal)
        return traversal
    def inorder_traversal(self,start,traversal):
        if start:
            
            traversal = self.inorder_traversal(start.left,traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.inorder_traversal(start.right,traversal)
        return traversal
    def postorder_traversal(self,start,traversal):
        if start:
            
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right,traversal)
            traversal += (str(start.value) + " - ")
        return traversal 
    def levelorder_print(self, start):
        if start is None:
            return 
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)       
        return traversal
    def reverselevelorder(self,start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue)>0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack)>0:
            node = stack.pop()
            traversal += str(node.value)
        return traversal
    def iterativepreorder(self,start):
        stack = Stack()
        stack.push(start)
        traversal = ""
        while len(stack)>0:
            node = stack.pop()
            traversal += str(node.value)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)     
        return traversal
    def iterativeinorder(self,start):
        stack = Stack()
        traversal = ""
        current = start
        while True:
            if current is not None:
                stack.push(current)
                current = current.left
            elif (stack):
                current = stack.pop()
                traversal += str(current.value)
                current = current.right
            else:
                break
        return traversal
    def size(self,start):
        stack = Stack()
        size = 0
        stack.push(start)
        while len(stack)>0:
            node = stack.pop()
            size +=1
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
        return size
    def sizerecursive(self,start):
        if start is None:
            return 0
        return 1 + self.sizerecursive(start.left) + self.sizerecursive(start.right)
    def heightrecursive(self,start):
        if start is None:
            return -1
        return 1 + max(self.heightrecursive(start.right) , self.heightrecursive(start.left))
    def height(self,start):
        if start is None:
            return 
        queue = Queue()
        height_left = 0
        height_right = 0
        queue.enqueue(start)
        while len(queue) > 0:
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
                height_left += 1
            if node.right:
                queue.enqueue(node.right) 
                height_right += 1      
        return max(height_left,height_right)-1

tree = Tree(1)
tree.root.left= Node(2)
tree.root.right= Node(3)
tree.root.left.left= Node(4)
tree.root.left.right= Node(5)
tree.root.right.left= Node(6)
tree.root.right.right = Node(7)
if __name__ == "__main__":
    print(tree.height(tree.root))
