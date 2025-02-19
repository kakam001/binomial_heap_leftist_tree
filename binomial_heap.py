class BinomialNode:
    def __init__(self, value):
        self.value = value
        self.order = 0
        self.parent = None
        self.children = []

    def __repr__(self):
        node_repr = f"(v={self.value}, o={self.order})"
        if self.children:
            children_repr = ", ".join(str(child) for child in self.children)
            node_repr += f" -> [{children_repr}]"
        return node_repr


class BinomialHeap:
    def __init__(self):
        self.root = None
        self.make_heap()

    def __repr__(self):
        node_repr = ""
        for i, node in enumerate(self.root):
            node_repr += f"{i+1}. {repr(node)}\n"
        return node_repr

    def make_heap(self):
        # rootlist to store all trees in
        self.root = []

    def minimum(self):
        if not self.root:
            return None

        minimum = self.root[0].value

        for heap in self.root:
            if heap.value <= minimum:
                minimum = heap.value

        return minimum

    def extract_min(self):
        if not self.root:
            return None

        min_iter = None
        min_children = None
        minimum = self.root[0].value

        i = 0
        for heap in self.root:
            if heap.value <= minimum:
                minimum = heap.value
                min_children = heap.children
                min_iter = i
            i += 1

        # delete the minimum out of the rootlist
        del self.root[min_iter]

        for child in min_children:
            child.parent = None

        # merge the children into the rootlist
        self.root = union(self.root, min_children)

    def insert(self, value):
        new_node = BinomialNode(value)
        new_list = [new_node]
        self.root = union(new_list, self.root)

        # returns a node --> easier to test --> delete / decrease_key function
        return new_node

    def decrease_key(self, node, new_value):
        # check if the new value is smaller than the current value
        if new_value <= node.value:
            node.value = new_value
        else:
            return

        # if there is no parent or the value is higher than the parent -> just end here
        if node.parent is None:
            return
        elif node.value >= node.parent.value:
            return

        # upheap change with parent if parent has a higher value
        cnt = node

        while cnt.parent is not None:
            parent = cnt.parent
            if cnt.value < parent.value:
                cnt_tmp_val = cnt.value
                cnt.value = parent.value
                parent.value = cnt_tmp_val

            cnt = cnt.parent

    def delete(self, node):
        # upheap the node (- infinity) to delete to remove it with extractmin
        self.decrease_key(node, -1000000)
        self.extract_min()


def union(heap1, heap2):
    # combine rootlist of heap1 and heap2
    rootlist = heap1
    rootlist.extend(heap2)
    rootlist.sort(key=lambda heap: heap.order)

    if rootlist is None:
        return []

    i = 0
    # go through the merged rootlist
    while i < len(rootlist) - 1:
        cnt = rootlist[i]
        nxt = rootlist[i + 1]

        # we want to merge the same order
        if cnt.order == nxt.order:
            # we look out for the case if we have three elements with the same order
            if i + 1 < len(rootlist) - 1 and rootlist[i + 2].order == nxt.order:
                nxt_nxt = rootlist[i + 2]
                if nxt.value < nxt_nxt.value:
                    nxt.children.append(nxt_nxt)
                    nxt.order = nxt.order + 1
                    nxt_nxt.parent = nxt
                    del rootlist[i + 2]
                else:
                    nxt_nxt.children.append(nxt)
                    nxt_nxt.order = nxt_nxt.order + 1
                    nxt.parent = nxt_nxt
                    del rootlist[i + 1]
            # in this case (two elements with same order) we just append the higher value to the smaller one
            else:
                if cnt.value < nxt.value:
                    cnt.children.append(nxt)
                    cnt.order = cnt.order + 1
                    nxt.parent = cnt
                    del rootlist[i + 1]
                else:
                    nxt.children.append(cnt)
                    nxt.order = nxt.order + 1
                    cnt.parent = nxt
                    del rootlist[i]
        else:
            # we only iterate by one if we do not have matching orders
            # this way we can merge the new resulting order with possible same orders after this one
            i = i + 1

    return rootlist


