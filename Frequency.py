
# === Class ===
class Frequency:
     def __init__(self):
         pass
    
     def twoSum(self, arr, target):
        if (len(arr) <= 0 or target is None): return [] 
        seen = {}
        for i, x in enumerate(arr):
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i
        return []
    
     def sortedTwoSum(self, arr, target):
         if (len(arr) <= 0 or target is None): return [] 
         lo, hi = 0, len(arr) - 1
         while lo < hi:
             mySum = arr[lo] + arr[hi]
             if mySum > target:
                 hi-=1
             elif mySum < target:
                 lo+=1
             elif mySum == target:
                 return [lo, hi]
         return []
                 
     def anagram(self, s, t):
         key = "".join(sorted(s))
         return ("".join(sorted(t)) == key)  
    
    
    
    
solver = Frequency()

# === Running ===
nums = [2, 7, 11, 15]
target = 9

print(solver.sortedTwoSum(nums, target))


