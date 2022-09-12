class SLNode:
    def __init__(self, val):
    self.value = val
    self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):	# added this line, takes a value
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self