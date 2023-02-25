'''
Given an array of positive integers representing the values of coins 
in your possession, write a function that returns the minimum amount 
of change (the minimum sum of money) that you cannot create. 

The given coins can have any positive integer value and aren't 
necessarily unique (i.e., you can have multiple coins of the same value).
'''

# we are expected to give the first number that cant be obtained by
# making a sum of the available coins


coins = [5, 7, 1, 1, 2, 3, 22]
output = 20

def nonConstructibleChange(coins):
    # We sort the list in ascending order because we have to return the
    # Minimum change possible
    coins.sort()
    # We define the minimum change as 0 by default
    change = 0

    for i in coins:
        # We check if the coin is greater than the current change plus one
        if i > change + 1:
            break
        # If not, we proceed to sum the list items to the change variable
        change += i
    # We return the minimum change possible plus one
    # As it turns it into the change that is not possible to create
    return change + 1

print(nonConstructibleChange(coins))