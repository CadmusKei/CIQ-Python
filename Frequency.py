
# === Class ===
class Frequency:
    def __init__(self):
        pass
    
    # == Hashmaps ==
    # = Two sum frequencies = 

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
    
    def topKFrequentElements(self, arr, k):
        if len(arr) < 1: return []
        freqMap = {}
        for x in arr:
            if x not in freqMap: freqMap[x] = 1
            else: freqMap[x]+=1
        sortedMap = (sorted(freqMap.items(), key= lambda item: item[1], reverse=True))
        # NB! Splitting dict[start:end]
        topK = sortedMap[:k] 
        # Construcut allowing extraction of single value in tuple      
        result = [num for num, freq in topK]
        return result
        # squares = [x**2 for x in nums]       
        # upper = [s.upper() for s in words] 
    
    # = Anagrams = 
    
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
            if freqMap.get(x, 0) >= 1: freqMap[x]-=1
            else:
                return False
        return True
    
     # NB: Group by X almost always means a key to group hashmap!!!
    def groupAnagrams(self, strs):
        if len(strs) < 1 or len(strs) > 100000: return []
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in groups: groups[key] = [word]
            else: groups[key].append(word)
        # or if list required list(groups.values())
        return groups.values()

        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
solver = Frequency()

# === Running ===
twoSumNums = [2, 7, 11, 15]
kNums = [4,4,4,5,5,6] 
k = 2
strs = ["eat","tea","tan","ate","nat","bat"]
target = 9
s = "anagram"
print(solver.topKFrequentElements(kNums, k))
