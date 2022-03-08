class Node:
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.head = None

  ## Method to display all elements inside the Linked List
  def print(self):
    if self.head is None:
      print("Linked List is empty")
      return
    iterator = self.head
    list_str = ' '
    while iterator:
      list_str += str(iterator.data)+ '-->'
      iterator = iterator.next_node
    print(list_str)

  ## Insertion of an element

  ## 1. Beginning of the Linked List
  ## Time Complexity : O(1)
  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node


 ## 2. End of the Linked List
  ## Time Complexity : O(n)
  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return

    iterator = self.head
    while iterator.next_node:
      iterator = iterator.next_node

    iterator.next_node = Node(data, None)


ll = LinkedList()
ll.insert_at_begining(10)
ll.insert_at_begining(20)
ll.insert_at_end(55)
ll.insert_at_begining(45)
ll.print()