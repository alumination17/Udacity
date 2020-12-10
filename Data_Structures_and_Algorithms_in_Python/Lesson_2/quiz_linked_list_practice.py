"""Since there is no built-in data structure in Python that looks like a linked list, 
we create a class representing linked lists  in Python."""

"""The LinkedList code from before is provided below. Add three functions to the LinkedList.
"get_position" returns the element at a certain position. The "insert" function will add an element to a particular
spot in the list. "delete" will delete the first element with that particular value.
Then, use "Test Run" and "Submit" to run the test cases at the bottom."""

class Element(object): # object inheritance is not important in Python 3.x but here it is left intentionally to keep the style of task
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


    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        current = self.head # current variable is set to the value of first element in a LinkedList
        counter = 1 # we need counter to track No of elements as we cannot return the length of LinkedList

        while current: # iterate through linked list until list won't end
            if counter == position: # check if first element is chosen (while counter = 1) 
                                    # or if counter is incremented enough to reach needed element
                return current # returning self.head (value of the first element in a LinkedList)
            else:       
                current = current.next # refer to the value of 'current.next' from aforementioned 'append' method
                counter += 1 # increment counter of LinkedList elements until the needed element is reached
            
        return None
            
    
    def insert(self, new_element, position):
        """Insert a new node at the given position. Assume the first position is "1".
        Inserting at position 3 means between the 2nd and 3rd elements."""
        
        current = self.head
        counter = 1

        if position == 1: 
                new_element.next = current # new element's's next value should link over to old head value (self.head)
                current = new_element # change the head pointer to the new one

        while counter < position - 1: # until we reach the previous position of aimed position
            current = current.next
            counter += 1
        ''' Once we reach the position of future inserted element, reassign ... ''' 
        new_element.next = current.next # Link shifted element with fresh inserted new element
        current.next = new_element # Override value of old element with value of new_element & link current element with the new one
        

    def delete(self, value):
        """Delete the first node with a given value."""
        
        current = self.head

        if current == None: return None # in self.head is None, returns None, there is nothing we can do with it
            
        if current.value == value: # if head (first node) value is the value we are going to delete...
            self.head = current.next  # assign a head status to the next node after head hence ignoring the old head
        # we must override 'self.next' value instead of 'current' because alternatively it will update 'current' variable but not 'head'
        else:
            while current.next: # walk through linked list until last element is NOT reached so there is something after
                # because if we reach last element, there is nothing after, but we need the next element to exist 
                if current.next.value == value: # if next element's value is the one we are looking for...
                    current.next = current.next.next # ...cut it out by walking around it
                    break
                else:
                    current = current.next # else: go to next element in the linked list

if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print (ll.head.next.next.value)
    # Should also print 3
    print (ll.get_position(3).value)

    # Test insert
    ll.insert(e4,3)
    # Should print 4 now
    print (ll.get_position(3).value)

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print (ll.get_position(1).value)
    # Should print 4 now
    print (ll.get_position(2).value)
    # Should print 3 now
    print (ll.get_position(3).value)