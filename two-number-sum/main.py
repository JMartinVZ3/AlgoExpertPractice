'''



'''

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
# [-1, 11]

def twoNumberSum(array, targetSum):
    for i in array:
        for j in array:
            sums = i + j
            if sums == targetSum and i != j:
                return [i, j]
    return []

print(twoNumberSum(array, targetSum))