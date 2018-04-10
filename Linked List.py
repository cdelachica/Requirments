class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, ndata):

        new_node = Node(ndata)

        new_node.next = self.head

        self.head = new_node

    def search(self, c):

        curr = self.head

        while curr != None:
            if curr.data == c:
                return True

            curr = curr.next

        return False

if __name__ == '__main__':

    ll = LinkedList()

    ll.push(11);
    ll.push(31);
    ll.push(12);
    ll.push(22);
    ll.push(15);

    if ll.search(30):
        print("Yes")
    else:
        print("No")
