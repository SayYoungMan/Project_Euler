'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

n = 1000  # Maximum number

res = 0  # Result sum
for i in range (1, 1000):
    if i % 3 == 0:  # If divisible by 3
        res += i
    elif i % 5 == 0:  # Elif to account for numbers that are both divisible by 3 and 5
        res += i

print(res)