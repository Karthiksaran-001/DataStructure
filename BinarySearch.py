
def BinarySearch(element , lst):
    if(len(lst) ==1 and lst[0] == element):
        return f"Element resent in 0 index"
    elif(len(lst) ==1 and lst[0] != element):
        return f"Element Not Present Inside the List"
    elif(len(lst) == 0):
        return f"List is Empty"
    else:
        lower = 0
        upper = len(lst) - 1
        sorted_lst = sorted(lst)
        while lower <= upper:
            mid = (lower + upper )//2
            if(sorted_lst[mid] == element):
                return f"Element Present inside the {mid} Index"
            else:
                if(sorted_lst[mid] < element):
                    lower = mid+1 
                else:
                    upper = mid  - 1 
        return f"Element Not Present"
        
        
lst = [i for i in range(10)]
print(lst)
print(BinarySearch(9 , lst))

        
        