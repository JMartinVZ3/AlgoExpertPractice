'''
Write a function that takes in a non-empty array of integers that are 
sorted in ascending order and returns a new array of the same 
length with the squares of the original integers also sorted in 
ascending order.
'''

array = [1, 2, 3, 5, 6, 8, 9]

#[1, 4, 9, 25, 36, 64, 81]

def sortedSquaredArray(array):
    lista = []
    for i in array:
        num = i ** 2
        lista.append(num)
    lista.sort()
    return lista


print(sortedSquaredArray(array))