def quick_sort(arr):     
  
  if len(arr) <= 1:     # edge case 
      return arr      
    
  pivot = arr[len(arr) // 2]   # it actually doesn't matter, you can define any element in the array as pivot   
  
  left_bucket = [x for x in arr if x < pivot]      # push all element less than pivot to left bucket 
  middle = [x for x in arr if x == pivot]   # middle is also a list   
  right_bucket = [x for x in arr if x > pivot]     # push all element greater than pivot to left bucket
  
  return quick_sort(left_bucket) + middle + quick_sort(right_bucket)  # apply quick sort to left and right bucket recursively 

arr = [54,26,93,17,77,31,44,55,20]  
quick_sort(arr)

>>> [17, 20, 26, 31, 44, 54, 55, 77, 93]
