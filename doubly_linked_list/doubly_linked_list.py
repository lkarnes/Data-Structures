"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    def find_middle(self):
        middle = self.head
        end = self.head
        while end != None:
            end = end.next.next
            if end != None:
                middle = middle.next
        return middle
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # wrap the given value in a ListNode
        new_node = ListNode(value, None, None)
        self.length += 1
        # handle if list has a head
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # handle if list has no head
        else:
            self.head = new_node
            self.tail = new_node
        #delete 
        #then add to head
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        node = self.head
        self.delete(self.head)
        return node.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # there is a tail
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        # there is no tail
        else:
            self.head = new_node
        self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        node = self.tail
        if self.tail == self.head:
            self.tail = None
            self.head = None
            self.length = 0
        if self.tail:
            self.tail.delete()
            self.length -= 1
            self.tail = self.tail.prev
            
        return node.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        new_node = node
        self.delete(node)
        self.length +=1
        new_node.prev = None
        new_node.next = self.head
        if self.tail == node:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.head.prev = new_node
        self.head = new_node
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head:
            print("you got nothing on me!")
            return
        self.length -= 1
        # if list has just one item
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # we have at least two nodes, and the node we want to delete is the head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        # we have at least two nodes, and the node we want to delete is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.delete()


    
        #is head
        #is tail
        #shrink length
        #
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        highest = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value >= highest:
                highest = current_node.value
            current_node = current_node.next
        return highest
