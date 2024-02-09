class TreeNode:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


class sortedmultiset:
    def __init__(self):
        """
        Created a node for balanced binary search and a list to store all elements in it
        """
        ##Created By Rushikesh Sunil Kotkar
        self.root = None
        self.multiset = []

    def insert(self, node, key):
        """
        Inserted an element in O(log n) times
        """
        ##Created By Rushikesh Sunil Kotkar
        if node is None:
            return TreeNode(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
            ##Created By Rushikesh Sunil Kotkar
        node = self.balfact(node)
        return node

    def erase(self, key):
        self.root = self.deleteele(self.root, key)

    def deleteele(self, node, key):
        """
        To delete an element in O(log n) Times
        """
        if node is None:
            return node
        elif key < node.key:
            node.left = self.deleteele(node.left, key)
        elif key > node.key:
            ##Created By Rushikesh Sunil Kotkar
            node.right = self.deleteele(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.minnode(node.right)
                node.key = successor.key
                ##Created By Rushikesh Sunil Kotkar
                node.right = self.deleteele(node.right, successor.key)
        node = self.balfact(node)
        return node

    def search(self, element):
        return self.searchele(self.root, element)

    def searchele(self, node, element):
        """
                To Search an element in O(log n) Times
                """
        if node is None or node.key == element:
            return node
        if element < node.key:
            ##Created By Rushikesh Sunil Kotkar
            return self.searchele(node.left, element)
        return self.searchele(node.right, element)

    def append(self, element):
        self.root = self.insert(self.root, element)
        self.multiset = []
        ##Created By Rushikesh Sunil Kotkar
        self.inorder(self.root, self.multiset)
        return self.multiset

    def inorder(self, node, result):
        """
                To Show elements in O(log n) Times
                """
        if node:
            self.inorder(node.left, result)
            result.append(node.key)
            ##Created By Rushikesh Sunil Kotkar
            self.inorder(node.right, result)

    def height(self, node):
        if node is None:
            return 0
        ##Created By Rushikesh Sunil Kotkar
        return 1 + max(self.height(node.left), self.height(node.right))

    def calcbalancefac(self, node):
        if node is None:
            ##Created By Rushikesh Sunil Kotkar
            return 0
        return self.height(node.left) - self.height(node.right)

    def leftro(self, node):
        rgh = node.right
        ##Created By Rushikesh Sunil Kotkar
        t = rgh.left

        rgh.left = node
        node.right = t

        return rgh

    def rightro(self, node):
        lft = node.left
        ##Created By Rushikesh Sunil Kotkar
        t = lft.right

        lft.right = node
        node.left = t

        return lft

    def balfact(self, node):
        if node is None:
            ##Created By Rushikesh Sunil Kotkar
            return node

        bal = self.calcbalancefac(node)

        if bal > 1:
            if self.calcbalancefac(node.left) < 0:
                ##Created By Rushikesh Sunil Kotkar
                node.left = self.leftro(node.left)
            return self.rightro(node)
        if bal < -1:
            if self.calcbalancefac(node.right) > 0:
                ##Created By Rushikesh Sunil Kotkar
                node.right = self.rightro(node.right)
            return self.leftro(node)
        return node
    def minnode(self, node):
        curr = node
        ##Created By Rushikesh Sunil Kotkar
        while curr.left:
            curr = curr.left
        return curr


"""
var_name=sortedmultiset()--->To create an object of sorted multiset
var_name.append(element:int)---> To add an element in  O(n)

"""
# ml = sortedmultiset()
# ml.append(10)
# ml.append(20)
# ml.append(30)
# ml.append(40)
# ml.append(50)
# print(ml.multiset)
