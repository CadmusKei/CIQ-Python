
class Greedy:
    def __init__(self):
        pass
    
    def islands(self, n, arr, limit):
        if len(arr) != n or arr is None: return []
        sortedArr = sorted(arr)
        resultArr = []
        lightest, heaviest = 0, len(sortedArr) - 1
        while lightest < heaviest:
            if (sortedArr[lightest] + sortedArr[heaviest] <= limit): 
                resultArr.append([arr[lightest], arr[heaviest]])
                lightest+=1
                heaviest-=1
            else:
                resultArr.append([arr[heaviest]])
                heaviest-=1
        return resultArr

solver = Greedy()
print(solver.islands(5, [3,6,8,1, 7], 10))
