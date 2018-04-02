class Stack:
  def __init__(self):
      self.items = ['Christian','Tan','Apple','Dela','Chica','Banana']

  def isEmpty(self):
      return self.items == [4]

  def push(self, item):
      return self.items.append(item)

  def pop(self):
      return self.items.pop(0)

  def peek(self):
      return self.items[0]

  def size(self):
      return len(self.items)

num = Stack()
num.push('Christian')
num.push('Tan')
num.push('Dela')

print(num.pop())
