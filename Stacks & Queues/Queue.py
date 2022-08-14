'''
Queue is Order Collection which we need to add from the last and delete from top
Stack works on FIFO
Important Stack Features are 
1. Enqueue Push(Add) 
2. Dequeue Pop(Remove)
3. Peek(Show)
4. Count
'''

'''
Application Of Stacks :
1. All the Process in our System Works on FIFO
'''

class Queue:
    lst =[]
    print("Queue is Created : ")
    def enqueue(self , item):
        self.lst.insert(0 , item)
        return(f"Item is Added Succesfully\nItems are {self.lst}")
    def dequeue(self):
        if(len(self.lst) < 1):
            return "Sorry List is Empty Please Try to add Item in Stack using Push"
        else:
            print(f"Removed item is : {self.lst.pop()}")
            return(f"Other Items are : {self.lst}")
    def peek(self , item):
        if(len(self.lst) <1):
            return "Sorry List is Empty Please Try to add Item in Stack using Push"
        else:
            try:
                return(f"The Item Based on the Index is {self.lst[item]}")
            except Exception as e:
                return(f"Sorry : {item} is Not Present in a List")
                
    def Count(self):
        return(f"The Count of the List is : {len(self.lst)}")


S = Queue()
print(S.enqueue("Apple"))
print(S.enqueue("Orange"))
print(S.enqueue("Banana"))
print(S.Count())
print(S.dequeue())
print(S.peek(5))

