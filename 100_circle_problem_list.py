# In a circle of 100 people if one person is killing the 2nd person and the 3rd person is killing 4th person..who lives at the end
# create a ircular linked list of 100 people

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, node):
        if not node:
            return

        if not self.head:
            self.head = node
            node.next = node
        else:
                
            # traverse to tail
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            
            # insert after tail
            tail.next, node.next = node, self.head

        self.count += 1


    def remove(self, node):
        """ removes node and returns next
        """
        print("removing ", node.data)

        if self.count == 0:
            raise Exception("no nodes to remove")

        if self.count == 1:
            if self.head == node:
                self.head = None
                self.count-=1
                return None
            else:
                raise Exception("node not found")
        else:
            # traverse to the node
            current, prev = self.head.next, self.head
            while current != node:
                prev, current = current, current.next
                
                if prev == self.head:
                    raise Exception("node not found")

            if current == self.head:
                # node is the first node to remove
                self.head = current.next
            
            prev.next = current.next
            self.count-=1
            return current.next


    def __repr__(self):
        print("Count=", self.count)

        res = ""
        current = self.head

        if not current:
            res += "(empty)"
            return res

        res += "("

        while True:
            res += str(current.data) + " --> "
            current = current.next
            if current == self.head:
                break
        
        res += ")\n"
        return res
        


if __name__ == "__main__":
    ll = LinkedList()

    for i in range(1, 101):
        ll.insert(Node(i))

    print(ll)

    current = ll.head
    while ll.count > 1:
        current = ll.remove(current.next)

    print(ll)
