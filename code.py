"""
This is the code file for Assignment from 23rd August 2017.
This is due on 30th August 2017.
"""
##################################################
#Complete the functions as specified by docstrings


# 1

def entries_less_than_ten(L):
    """
    Return those elements of L which are less than ten.

    Args:
        L: a list

    Returns:
        A sublist of L consisting of those entries which are less than 10.
    """
    return [i for i in L if i < 10]#Add your code here

#Test
#print entries_less_than_ten([2, 13, 4, 6, -5]) == [2, 4, 6, -5]

# 2

def number_of_negatives(L):
    """
    Return the number of negative numbers in L.

    Args:
        L: list of integers

    Returns:
        number of entries of L which are negative
    """
    return sum(i<0 for i in L)##YOUR CODE REPLACES THIS

# TEST
#print number_of_negatives([2, -1, 3, 0, -1, 0, -45, 21]) == 3

# 3
def common_elements(L1, L2):
    """
    Return the common elements of lists ``L1`` and ``L2``.

    Args:
        L1: List
        L2: List

    Returns:
        A list whose elements are the common elements of ``L1`` and
        ``L2`` WITHOUT DUPLICATES.
    """
    return list(set(L1).intersection(L2)) # your code goes here

#TEST
#print common_elements([1, 2, 1, 4, "bio", 6, 1], [4, 4, 2, 1, 3, 5]) == [1, 2, 4]

#4
def fibonacci_generator():
    """
    Generate the Fibonacci sequence.

    The Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21,...
    is defined by a1=1, a2=1, and an = a(n-1) + a(n-2).
    """
    i,j=1,1
    while True:
        yield i
        i,j=j,i+j# Hint: use the ``yield`` command.

#TEST
f = fibonacci_generator()
#print f.next(),f.next(),f.next(),f.next(),f.next(),f.next(),f.next(),f.next(),f.next(),f.next()
#[f.next() for f in range(10)] #== [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#5
def largest_fibonacci_before(n):
    """
    Return the largest Fibonacci number less than ``n``.
    """
    f=fibonacci_generator()
    i=f.next()
    j=f.next()
    while j<n:
        i=j
        j=f.next() #Your code goes here.
    return i

#TEST
#print largest_fibonacci_before(55) == 34

#6
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def catalan_generator():
    """
    Generate the sequence of Catalan numbers.

    For the definition of the Catalan number sequence see `OEIS <https://www.oeis.org/A000108>`.
    """
    i=0
    while True:
        yield fact(2*i)/(fact(i)*fact(i+1))#Your code goes here.
        i+=1

#TEST
#c = catalan_generator()
#print [c.next() for i in range(10)] #== [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]

    
    
#7
### CREATE YOUR OWN FUNCTION. Make sure it has a nice docstring.
# See https://www.python.org/dev/peps/pep-0257/
# for basic tips on docstrings.
