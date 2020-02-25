"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

start = time.perf_counter()

def palin (st):
    length = len(st)
    if length % 2 == 0: #Even Cases
        front = st[:int(length/2)]
        back = st[int(length/2):]
        if front == back[::-1]:
            return True
    else: #Odd Cases
        front = st[:int((length-1)/2)]
        back = st[int((length-1)/2):]
        if front == reversed(back):
            return True
    return False

largest = 0
for i in range (100, 1000):
    for j in range (100, 1000):
        prod = i*j
        if palin(str(prod)) == True:
            if prod > largest:
                largest = prod

print(largest)
print(time.perf_counter() - start, "seconds")