
def BinarySearch(arr , i , j , x ):
    
    while(i <= j):
        mid = (i + j)//2
        if(x == arr[mid]):
            return mid
            break
        elif(x > arr[mid]):
            i = mid+1
        else:
            j = mid-1
    return -1  
    

       
       
       
arr = [10, 23,35,67,75,86,90,95]
i = 0
j = len(arr)-1
x = 87
print(BinarySearch(arr , i , j , x ))   