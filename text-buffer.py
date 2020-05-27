



import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class TextBuffer: 
    def __init__(self):
        self.storage = DoublyLinkedList()
    def __str__(self):
        current_node = self.storage.head
        string_return = ''
        while current_node != None:
            string_return += current_node.value
            current_node = current_node.next
        return string_return

    def append(self, string):
        for char in string:
            self.storage.add_to_tail(char)

    def prepend(self, string):
        for char in string:
            self.storage.add_to_head(char)

    def join(self, other_buffer):
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        self.storage.tail = other_buffer.storage.tail
        
    def delete_from_back(self, amount):
        for _ in range(amount):
            self.storage.remove_from_tail()

    def delete_from_front(self, amount):
        for _ in range(amount):
            self.storage.remove_from_head()

    def find_text(self, text):
        pass
    

text = TextBuffer()
text.append('hello ')
other = TextBuffer()
other.append('whats your name')

text.join(other)
print(text)

