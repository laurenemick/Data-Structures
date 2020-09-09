"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # check if there is no head 
        if not self.head and not self.tail:
            new_node = ListNode(value, None, None)
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the head
        else:
            new_node = ListNode(value, None, self.head)
            # set the current head's previous reference to our new node
            self.head.prev = new_node
            # set the list's head reference to the new node
            self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.next:
            head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return head.value
        # otherwise we have more than one element in our list
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            new_node = ListNode(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        if not self.head.next:
            tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return tail.value
        value = self.tail.value
        self.tail = self.tail.prev
        self.length -= 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node == self.tail:
            head = self.head
            self.tail = self.tail.prev
            self.head.prev = node
            self.head = node
            self.head.next = head
        else:
            head = self.head
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = node
            self.head = node
            self.head.next = head

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.head:
            self.head = self.head.next
            tail = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.prev = tail
            
        else:
            self.head = self.head.next
            tail = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.prev = tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head.next and node == self.head:
            self.head = None
            self.tail = None
            self.length = 0
        elif node == self.head: 
            self.head = node.next
            self.length -= 1
        elif node == self.tail: 
            self.tail = node.previous
            self.length -= 1
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value