    class Sort:
      def __init__(self, list_):
          self.list = list_

      def quickSort(self):      
        pivot = -1
        arr = self.list
        
        def quickSortRecurse(arr):
          l, r = 0, len(arr) - 2
          
          # print("recursing :::::::::::::::::::::", arr)
          # print("original  :::::::::::::::::::::", self.list)
          if len(arr) < 3:
            if arr[0] > arr[-1]:
              arr[0], arr[-1] = arr[-1], arr[0]
            return arr
          

          while l < r:
            # print(arr, l, r)
            if arr[l] < arr[pivot]:
              l += 1
            if arr[r] > arr[pivot]:
              r -= 1
            if arr[l] > arr[pivot] and arr[r] < arr[pivot]:
              arr[l], arr[r] = arr[r], arr[l]
              l += 1
              r -= 1

          if l == r:
            # print(arr, arr[pivot], l, r, pivot)
            while arr[l] <= arr[pivot]:
                l += 1
            arr[pivot], arr[l] = arr[l], arr[pivot]
            # print(f"swap : {arr[pivot]}, pivot : {arr[l]}")
            # print("---------------------------------------------",arr)
          
          left, right = arr[:l], arr[l+1:]
          
          quickSortRecurse(left)
          quickSortRecurse(right)        
          
          return arr
            
        
        return quickSortRecurse(self.list) 