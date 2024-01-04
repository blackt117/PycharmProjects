##############
# Name: Tyler Black
# Due Date: 5/1/23
# No need to grade. I wanted to practice BST and understand it a little more without using the book's code
#
#
##########################




def helpright(node):

    while node.left != None:
      node = node.left
    return node

class Node():
    def __init__(self, data = None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def __str__(self):
        return "[%s, %s, %s]" % (self.left, str(self.data), self.right)


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    

class BST():
    def __init__(self):
        self.root = None
        self.count = 0
        self.max = 0
        self.height = 0

    def is_empty(self):
        return self.root == None

    def __len__(self):
        return self.count

    def insert(self,item):
        newNode=Node(item)
        self.count += 1
        if self.is_empty():
            self.root = newNode
        else:
            temp = self.root
            while temp != None:
                if newNode.data < temp.data:
                    if temp.left == None:
                        temp.left = newNode
                        if temp.right == None:
                            self.height += 1
                        temp=None
                    else:
                        temp=temp.left
                else:
                    if temp.right == None:
                        temp.right = newNode
                        if temp.left == None:
                            self.height += 1
                        temp=None
                    else:
                        temp=temp.right



    def __contains__(self,item):
        newNode = Node(item)
        temp = self.root
        while temp != None:
            if newNode.data < temp.data:
                temp = temp.left
            elif newNode.data > temp.data:
                temp = temp.right
            else:
                return True
        return False

    def max_height(self):
        return self.height

    def _preorder(self, root):
        if root:
            print(root.data)
            self._preorder(root.left)
            self._preorder(root.right)

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.data)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.data)
            self._inorder(root.right)

    def traverse_preorder(self, node=None):
        if node == None:
            node=self.root
        else:
            node = node
        self._preorder(node)

    def traverse_postorder(self, node=None):
        if node == None:
            node=self.root
        else:
            node=node
        self._postorder(node)

    def traverse_inorder(self, node = None):
        if node == None:
            node = self.root
        else:
            node = node
        self._inorder(node)

    def remove(self,value):
        if self.root == None:
            return None
        if self.count == 1 and value==self.root.data:
            temp = self.root
            self.root = None
            self.count = self.count - 1
            return temp
        if self.count == 1 and value != self.root.data:
            return None
        parent = self.root
        current = self.root
        while current != None:
            if value < current.data:
                    parent = current
                    current = current.left
            elif value > current.data:
                    parent = current
                    current = current.right
            else:
                if current.right == None and current.left ==None:
                    if value > parent.data:
                        parent.right = None
                        self.count = self.count - 1
                        return current
                    else:
                        parent.left = None
                        self.count = self.count - 1
                        return current
                elif current.left != None:
                    if value == current.data and value == parent.data:
                        temp = current.left
                        self.root = current.left
                        if temp.right !=None and current.right!=None:
                            temp.right.right = current.right
                            self.count = self.count - 1
                            return current
                        self.root.right = current.right
                        self.count = self.count - 1
                        return current
                    elif value > parent.data:
                        temp = current.left
                        parent.right = current.left
                        if temp.right == None:
                            temp.right = current.right
                            self.count = self.count - 1
                            return current
                        else:
                            temp2 = temp.right
                            temp2.right = current.right
                            self.count = self.count - 1
                            return current
                    else:
                        temp = current.left
                        parent.left = current.left
                        temp.right = current.right
                        self.count = self.count - 1
                        return current
                else:
                    if value == current.data and value == parent.data:
                        node = helpright(current.right)
                        tempright = current.right
                        temp1 = node.right
                        self.root = node
                        if current.right == node:
                            self.root.left == None
                            self.root.right = node.right
                            self.count = self.count - 1
                            return current
                        else:
                            if node.right != None:
                                temp1.right = tempright
                                tempright.left = None
                            else:
                                self.root.right = tempright
                                tempright.left=None
                            self.count = self.count - 1
                            return current
                    elif value > parent.data:
                        node = helpright(current.right)
                        if current.right == node:
                            parent.right = node
                            self.count = self.count - 1
                            return current
                        temp1 = current.right
                        temp2 = node.right
                        temp1.left = None
                        parent.right = node
                        if node.right == None:
                            node.right = temp1
                            self.count = self.count - 1
                            return current
                        else:
                            temp2.right = temp1
                            self.count = self.count - 1
                            return current
                    else:
                        node = helpright(current.right)
                        parent.left = node
                        self.count = self.count - 1
                        return current
        if current == None:
            return None

    def helper_right(self,node):
        if node.right:
            return self.helper_right(node.right)
        else:
            return node.data


    def find_max(self):
        if self.is_empty() == True:
            return None
        if self.root.right:
            return self.helper_right(self.root.right)
        else:
            return self.root.data







        






