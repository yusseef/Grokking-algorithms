def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2 #Get middle value
        guess = lst[mid] 
        if guess == item:
            return mid
        elif guess > item: #Too high 
            high = mid -  1
        else:
            low = mid + 1
    return None

#Complexity ==> O(log2​(n))