"""
You're about to do an assignment called "Fizz Buzz", which is one of the classic programming challenges. It is a favorite for interviewers, 
and a shocking number of job-applicants can't get it right. But you won't be one of those people. Here are the rules for the assignment (as specified by Imran Gory):

Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".
"""


for l in range(1,101): 
    if l % 3 == 0 and l % 5 == 0: 
        print(l)
        print("Fizzbuzz")
        continue 
    elif l % 3 == 0: 
        print(l)
        print("Buzz") 
        continue 
    elif l % 5 == 0: 
        print(l)
        print("Fizz") 
        continue
    #prime number
    """
    elif l % l == 0 and l % 1 == 0:
        print("Prime")
        continue
    """
    print(l)