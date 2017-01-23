#!/usr/local/bin/python3

def factors(num):
    n = 1
    while n <= num:
        if num%n==0:
            print("{} is a divisior of {}".format(n,num))
        n = n + 1

if __name__ == "__main__":
    x = int(input("Enter a positive integer: "))
    factors(x)
            

        
        
