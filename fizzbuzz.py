#Write a Python program that iterates the integers from 1 to 50. 
#For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
#For numbers that are multiples of three and five, print "FizzBuzz".

def vFnFizzBuzz():
    #import pdb; pdb.set_trace()
    for i in range(1,51):
        strout = ""
        if i%3 == 0 :
            strout += "Fizz"
        if i%5 == 0:
             strout += "Buzz"
        print(strout)

vFnFizzBuzz()