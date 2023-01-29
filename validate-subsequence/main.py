'''
Given two non-empty arrays of integers, write a function that determines 
whether the second array is a subsequence of the first one.
'''

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
# expected output: true

def validateSubsequence(array, sequence):
    # Eliminate different items
    lista = [x for x in array if x in sequence]

    while len(lista) > len(sequence):
        lista.pop()

    # After eliminating the extra items, check if lists are equal
    if lista == sequence:
        return True
    return False

#true
print(validateSubsequence(array, sequence))