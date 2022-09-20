class DLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, val):
        new_node = DLNode(val)
        current_head = self.head
        self.head.prev = new_node
        new_node.next = current_head
        self.head = new_node	# SET the list's head TO the node we created in the last step
        if self.tail == None:
            self.tail = new_node
        return self	# return self to allow for chaining


    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self	# once the loop is done, return self to allow for chaining

    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
            self.tail = DLNode(val)
            return self	# let's make sure the rest of this function doesn't happen if we add to the front
        new_node = DLNode(val)
        new_node.prev = self.tail
        current_tail = self.tail
        current_tail.next = new_node
        self.tail = new_node
        return self     # return self to allow for chaining

    def remove_from_front(self):
        self.head = self.head.next
        return self

    def remove_from_back(self):
        self.tail = self.tail.prev
        self.tail.next = None
        return self

    def remove_val(self, val):
        if self.head.value == val: # first node
            self.remove_from_front()
            return self
        elif self.tail.value == val:
            self.remove_from_back()
        runner = self.head
        while (runner.next != None):
            if runner.next.value == val:
                break
            runner = runner.next

        
        if runner.next == None:
            print(f'Value {val} cannot be found')
        elif runner.next.value == val: # skip the value to remove, if at the end, then next = None
            runner.next = runner.next.next
            runner.next.prev = runner
        
        return self
        
    def insert_at(self, val, n):
        new_node = DLNode(val)
        if n == 0:
            self.add_to_front(val)
        counter = 1
        node_before = self.head
        while counter != n:
            node_before = node_before.next
            counter += 1
        new_node.next = node_before.next
        node_before.next.prev = new_node
        new_node.prev = node_before
        node_before.next = new_node
        return self

