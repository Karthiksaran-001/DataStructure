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
      list_str += str(iterator.data) + '-->'
      iterator = iterator.next_node
    print(list_str)

  ## Insertion of an element

  ## 1. Beginning of the Linked List
  ## Time Complexity : O(1)
  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node


ll = LinkedList()
ll.insert_at_begining(10)
ll.insert_at_begining(20)
ll.print()