

class LeftNode:
    def __init__(self, value=0, left_node=None, right_node=None, distance=0):
        self.value = value
        self.distance = distance
        self.left_child = left_node
        self.right_child = right_node
        self.parent = None

    def __repr__(self):
        lines = []
        if self.right_child:
            found = False
            for line in repr(self.right_child).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(f"v: {self.value} d: {self.distance}")
        if self.left_child:
            found = False
            for line in repr(self.left_child).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


class LeftistTree:
    def __init__(self, leftist_node=None):
        if leftist_node is not None:
            self.root = leftist_node
        else:
            self.make_heap()

    def __repr__(self):
        return repr(self.root)

    def is_empty(self):
        return self.root is None

    def make_heap(self):
        self.root = LeftNode()

    def minimum(self):
        return self.root.value

    def insert(self, value):
        l_node = LeftNode(value=value, distance=1)
        l_tree = LeftistTree(leftist_node=l_node)
        self.root = union(self.root, l_tree.root)

        # returns a node --> easier to test --> delete / decrease_key function
        return l_node

    def extract_min(self):
        minimum = self.root.value

        d1 = self.root.left_child
        d2 = self.root.right_child

        self.root = union(d1, d2)

        return minimum

    def delete(self, del_node):
        del_left = None
        del_right = None

        # if parent is none, we are at the minimum position
        if del_node.parent is None:
            self.extract_min()
            return

        del_tree_left = LeftistTree(leftist_node=None)
        del_tree_right = LeftistTree(leftist_node=None)

        # get trees for the remaining left child and right child
        if del_node.left_child is not None:
            del_left = del_node.left_child
            del_left.parent = None
            del_tree_left = LeftistTree(leftist_node=del_left)
        if del_node.right_child is not None:
            del_right = del_node.right_child
            del_right.parent = None
            del_tree_right = LeftistTree(leftist_node=del_right)

        # if a right child is present check if we are the right child or not and change dependencies
        if del_node.parent.right_child is not None:
            if del_node.parent.right_child != del_node:
                del_node.parent.left_child = del_node.parent.right_child
                del_node.parent.right_child = None
                del_node.parent.distance = 1
            else:
                del_node.parent.right_child = None
                del_node.parent.distance = 1
        else:
            del_node.parent.left_child = None

        # use the parent param to move to the top of the tree and change the right and left child accordingly
        upheap = del_node.parent
        while upheap.parent is not None:
            if upheap.parent.right_child == upheap:
                if upheap.parent.right_child.distance > upheap.parent.left_child.distance:
                    tmp_left = upheap.parent.left_child
                    upheap.parent.left_child = upheap.parent.right_child
                    upheap.parent.right_child = tmp_left
            if upheap.parent.right_child is not None:
                upheap.parent.distance = upheap.parent.right_child.distance + 1
            else:
                upheap.parent.distance = 1

            upheap = upheap.parent

        # remove all leftover params
        del_node.parent = None
        del_node.left_child = None
        del_node.right_child = None
        del_node.distance = None
        del_node.value = None

        # put the remaining children (trees) of the deleted node back into the leftist tree with unions
        if del_left is not None:
            self.root = union(self.root, del_tree_left.root)
        if del_right is not None:
            self.root = union(self.root, del_tree_right.root)

    def decrease_key(self, dec_node, new_val):
        self.delete(dec_node)
        self.insert(new_val)


def union(d1, d2):
    # termination conditions if one is None return the other
    if d1 is None or d1.distance == 0:
        return d2
    if d2 is None or d2.distance == 0:
        return d1

    # change the order of the union operation if d1 has a higher val than d2
    if d1.value > d2.value:
        return union(d2, d1)

    # recursively merge the right child with d2
    d1.right_child = union(d1.right_child, d2)
    d1.right_child.parent = d1

    # look out for the leftist condition if there is no left child
    if d1.left_child is None:
        d1.left_child = d1.right_child
        d1.right_child = None
        d1.distance = 1

        d1.left_child.parent = d1
        return d1

    # if the right distance is higher -> change to remain the leftist condition (distance)
    if d1.right_child.distance > d1.left_child.distance:
        tmp_node = LeftNode(d1.left_child.value, d1.left_child.left_child, d1.left_child.right_child,
                            d1.left_child.distance)
        d1.left_child = d1.right_child
        d1.right_child = tmp_node

        d1.left_child.parent = d1
        d1.right_child.parent = d1

    d1.distance = d1.right_child.distance + 1
    return d1
