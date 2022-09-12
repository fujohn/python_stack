class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node	# SET the list's head TO the node we created in the last step
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
            return self	# let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	# increment the runner to the next node in the list
        return self     # return self to allow for chaining

    def remove_from_front(self):
        self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None:
            return self
        runner = self.head
        while (runner.next.next != None):
            runner = runner.next
        runner.next = None
        return self

    def remove_val(self, val):
        if self.head.value == val: # first node
            self.remove_from_front()
            return self
        runner = self.head
        while (runner.next != None):
            if runner.next.value == val:
                break
            runner = runner.next
        
        if runner.next == None:
            print(f'Value {val} cannot be found')
        elif runner.next.value == val: # skip the value to remove, if at the end, then next = None
            runner.next = runner.next.next
        
        return self
        
    def insert_at(self, val, n):
        new_node = SLNode(val)
        if n == 0:
            self.add_to_front(val)
        counter = 1
        node_before = self.head
        while counter != n:
            node_before = node_before.next
            counter += 1
        new_node.next = node_before.next
        node_before.next = new_node
        return self




my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").insert_at('test', 1).print_values() # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!


