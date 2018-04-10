class Queue:
        def __init__(self):
            self.items = []
        def isEmpty(self):
            return self.items == []

        def enqueue(self,item):
            return self.items.insert(0,item)
        def dequeue(self):
            return self.items.pop()
        def size(self):
            return len(self.items)
        def peek(self,i):
            return self.items[i]

if __name__ =="__main__":

    places_to_go = Queue()
    places_to_go.enqueue("Sagada")
    places_to_go.enqueue("Batangas beach")
    places_to_go.enqueue("Oslob Ceu")
    places_to_go.enqueue("Siargao Island")
    places_to_go.enqueue("Palawan")
    places_to_go.enqueue("Man-made forest in Bohol")
    places_to_go.enqueue("Camiguin Island")
    print (places_to_go.items)

    places_to_go.dequeue()
    places_to_go.dequeue()
    print (places_to_go.items)