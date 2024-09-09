def sort_array(arr):
    try:
        low, mid, high = 0, 0, len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]  # Swap 0
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1  
            else:
                arr[mid], arr[high] = arr[high], arr[mid]  # Swap 2
                high -= 1

        return arr  # Return the sorted array

    except Exception as e:
        print(f"An error occurred: {e}")
        return []  # Return an empty list in case of an error

# Test cases
# print(sort_array([0, 1, 2, 1, 0, 2, 1, 0]))  
# print(sort_array([2, 2, 2, 2]))              
# print(sort_array([0, 0, 0, 0]))              
# print(sort_array([1, 1, 1, 1]))            
# print(sort_array([2, 0, 1]))                 
# print(sort_array([]))                        
