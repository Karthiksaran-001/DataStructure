## Linear Search

def LinearSearch(arr , searchElement , n):
    for i in range(n):
        if arr[i] == search_Element:
            return(f"Element {search_Element} is Found at : {i} index")
    else :
        return(f"Sorry Element {searchElement} Not Found")





## declare an Array :
arr = [53, 12 , 32 , 17 , 39 , 90]
search_Element = 11
Length = len(arr)
print(LinearSearch(arr , search_Element  , Length))## not found
search_Element = 32
print(LinearSearch(arr , search_Element  , Length)) ## found