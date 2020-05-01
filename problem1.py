#! coding:utf-8

"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


# Define Function

def function(array, k):
    taille = len(array)
    exits = False
    for i in range(taille):
        for j in range(i+1, taille):
            if (array[i] + array[j] == k):
                exits = True
    return print(exits)

# Bonus
def func_bonus(array, k):
    taille = len(array)
    exits = False
    for i in range(taille):
        num = abs(array[i] - k)
        if k % array[i] == 0:
            pass
        elif num in array:
            exits = True
    return print(exits)

# Test
if __name__ == '__main__':
    array = [10,15,3,7]
    k = 17

    function(array, k)
    func_bonus(array,k)