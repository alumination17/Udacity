"""Add a couple methods to our LinkedList class, and use that to implement a Stack.
You have 4 functions below to fill in: insert_first, delete_first, push, and pop.
Think about this while you're implementing: why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head #  link new element's 'next' attribute to current self_head element 
        self.head = new_element # self_head becomes the new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList and return it"
        # current = self.head 
        current = self.head # variable 'current' is set to the value of first ('head') element in a LinkedList

        if self.head: # if self.head exists > we can assign self-head.next to self_head value and delete the old self.next
            self.head = current.next
            return current
        else:
            return None


class Stack(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print (Stack().pop().value)
print (Stack().pop().value)
print (Stack().pop().value)
print (Stack().pop())
print (Stack().pop().value)