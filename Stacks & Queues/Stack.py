'''
Stack is Order Collection which we need to add and delete the item in top
Stack works on LIFO
Important Stack Features are 
1. Pop(Remove)
2. Push(Add)
3. Peek(Show)
4. Count
'''

'''
Application Of Stacks :
1. All Our Browsing History Stored in Stack Order
'''



class Stack:
    lst =[]
    def push(self , num):
        self.lst.append(num)
        return(f"Item is Added Succesfully\nItems are {self.lst}")
    def Pop(self):
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


S = Stack()
print(S.push("Apple"))
print(S.push("Orange"))
print(S.push("Banana"))
print(S.Count())
print(S.Pop())
print(S.peek(5))


