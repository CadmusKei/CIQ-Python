
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
             if mySum > target: hi-=1
             elif mySum < target: lo+=1
             elif mySum == target: return [lo, hi]
         return []
     
     def firstUniqueCharacter(self, str):
         if str is None: return -1
         freqmap = {}
         for x in str:
             if x not in freqmap:
                 freqmap[x] = 1
             else: freqmap[x] += 1 
         for i, x in enumerate(str):
             if freqmap[x] == 1: return i
         return -1
                
     # O(n) solution to anagram which doesn't sort
     def anagram(self, s, t):
         if len(s) != len(t):
            return False
            
         freqMap = {}
         for x in s:
             if x not in freqMap:
                freqMap[x] = 1
             else: 
                freqMap[x]+=1
         for x in t:
             if freqMap.get(x, 0) >= 1: freqMap[x]-=1;
             else:
                return False
         return True
     

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    
    
solver = Frequency()

# === Running ===
nums = [2, 7, 11, 15]
target = 9

print(solver.firstUniqueCharacter("anagram"))
