class HeapNode:
    """
    Represents a single node in binary tree min-heap
    Each node holds:
    + distance
    + node_id  : which graph node this refers to

    + left     : pointer to left child node, None if no left child
    + right    : pointer to right child node, None if no right child
    + parent   : pointer to parent node, None if this is the root
    """

    def __init__(self, distance, node_id):
        self.distance = distance
        self.node_id = node_id
        self.left = None
        self.right = None
        self.parent = None

