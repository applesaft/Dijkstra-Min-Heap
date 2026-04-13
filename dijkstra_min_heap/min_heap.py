from heap_node import *

class MinHeap:
    """
    A min-heap implemented as a proper binary tree using HeapNode objects
    Invariant,
        parent.distance <= children.distance
        (the node with the smallest distance is always at the root)
    """

    def __init__(self):
        self.root = None
        self.size = 0 # Size of Tree

    def insert_node(self, distance, node_id):
        """
        Insert a new node into the heap:
        + Preserve shape: place the new node in the next available position, left to right
                          (We find this position using the binary representation of (size + 1))
        + Satisfying invariant
        """

        new_node = HeapNode(distance, node_id)
    
        # Use binary representation of (size + 1) to find the exact path to the insertion position.
        binary = str(bin(self.size + 1))[3:]
        if binary == '':
            self.root = new_node
            self.size = self.size + 1
            return
        
        current = self.root
        i = 0  
        while i < len(binary):
            character = binary[i]

            if i == len(binary) - 1:
                if character == '0':
                    current.left = new_node
                else:
                    current.right = new_node
                new_node.parent = current

            else:
                if character == '0':
                    current = current.left
                else:
                    current = current.right

            i = i + 1

        self.size = self.size + 1
        self.sort_up(new_node)


    def sort_up(self, node):
        """
        Restore the heap order after insertion 
        We compare the node with its parent and swap values if the node's distance is smaller than its parent's.
        We keep swapping (values) until either:
            + The node reaches the root (no more parent)
            + The invariant is satisfied
        """

        current = node
        while current.parent is not None:
            if current.distance < current.parent.distance:
                current.distance, current.parent.distance = (current.parent.distance, current.distance)

                current.node_id, current.parent.node_id = (current.parent.node_id, current.node_id)
                current = current.parent
            else:
                break

    # helper function
    def delete_node(self):
        # find last node
        binary = str(bin(self.size))[3:]

        current = self.root
        i = 0
    
        while i < len(binary):  
            character = binary[i]
        
            if character == '0':
                current = current.left
            else:
                current = current.right
            i = i + 1

        return current

    def sort_down(self, node):
        """
        Restore heap order after deletion 
        compare the node with its smallest child
        keep swapping until either:
        + The node has no children (we reached a leaf)
        + Invariant is satisfied (parent <= children)
        """
        # current should be new root node
        current = node
        while True:
            smallest = current
            if (current.left is not None and current.left.distance < smallest.distance):
                smallest = current.left

            if (current.right is not None and current.right.distance < smallest.distance):
                smallest = current.right

            if smallest == current:
                break

            current.distance, smallest.distance = (smallest.distance, current.distance)
            current.node_id, smallest.node_id = (smallest.node_id, current.node_id)
            current = smallest

    def extract_min(self): # remove and return the root node
        if self.root is None:
            return None 

        min_distance = self.root.distance
        min_node_id = self.root.node_id

        last_node = self.delete_node()
        self.root.distance = last_node.distance
        self.root.node_id = last_node.node_id

        # removing the last node from the tree
        if last_node.parent.right == last_node:
            last_node.parent.right = None
        else:
            last_node.parent.left = None

        self.size = self.size - 1
        self.sort_down(self.root)
        return (min_distance, min_node_id)
    
    def is_empty(self): # checks if heap is empty
        return self.root is None