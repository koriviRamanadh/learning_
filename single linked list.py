class Node:
    
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next 

class Linked_list:


    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        itr = self.head
        while itr.next != None:
             itr = itr.next

        node = Node(data)
        itr.next = node

    def insert_at_left(self,elem,data):
        if self.head.data == elem:
            node = Node(data)
            node.next = self.head
            self.head = node
        else:
            itr = self.head
            prev = self.head
            while itr:
                if itr.data == elem:
                    break 
                prev = itr 
                itr = itr.next

            node = Node(data)
            node.next = itr
            prev.next = node


    def insert_at_right(self,elem,data):
        itr = self.head
        while itr:
            if itr.data == elem:
                break
            itr = itr.next
        
        node = Node(data,itr.next)
        itr.next = node

    def delete_at_end(self):
        itr = self.head
        prev = None
        while itr.next != None:
            prev = itr
            itr = itr.next
        del itr 
        prev.next = None

    def delete_at_begining(self):
        itr = self.head
        self.head = itr.next
        del itr

    def pop(self, elem):

        if self.head.data == elem:
            itr = self.head
            self.head = itr.next
            del itr
        else:
            itr = self.head.next 
            prev = self.head
            while itr:
                if itr.data == elem:
                    break
                prev = itr 
                itr = itr.next
            if(itr == None):
                print("The element is not found")
            else:
                prev.next = itr.next
                del itr

    def show(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        llstr = ''

        while itr:

            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)


if __name__ == '__main__':
    ll = Linked_list()
    ll.insert_at_begining(5)
    ll.insert_at_end(10)
    ll.insert_at_right(5,7)
    ll.insert_at_left(5,4)
    ll.insert_at_left(10,8)
    ll.insert_at_right(10,9)
    ll.pop(4)
    ll.pop(9)
    ll.pop(8)
    ll.show()