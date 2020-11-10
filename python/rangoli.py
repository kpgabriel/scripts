import string
from collections import deque


def print_rangoli(n):
    # your code goes here
    """ Function that returns a pattern """
    alpha = string.ascii_lowercase
    L = []

    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append(s[::-1]+s[1:])
   
    width = len(L[0])

    for i in range(n-1, 0, -1):
        print(L[i].center(width, "-"))

    for i in range(n):
        print(L[i].center(width, "-"))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)