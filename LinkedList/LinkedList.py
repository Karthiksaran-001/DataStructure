class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    ## Insert Data at Begining 
    def push(self , new_value):
        new_node = Node(new_value) ## Create new Node 
        new_node.next = self.head 
        ## Previously Head Point To Null Now our new node point to Null
        self.head = new_node


    ##Insert data at any position 
    def insertAt(self , prev_node , new_value): ## Without knowing Previous node we cant insert
        if(prev_node is None):
            print("Previous Node is Empty")
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    
    ## Insert at the End
    def insertAtEnd(self , new_value):
        new_node = Node(new_value)

        #check the LinkedList is Empty
        if self.head is None:
            self.head = new_value
            return
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_value
    
    # just for demo
    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insertAtEnd(5)
    llist.push(10)
    llist.printlist()