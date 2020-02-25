"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p**2 <= n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return prime

n = 1000000
prime = SieveOfEratosthenes(n)
no = 0
for i in range(2,n):
    if prime[i]:
        no += 1
    if no == 10001:
        print(f'10001th Prime Number is: {i}')
        break

