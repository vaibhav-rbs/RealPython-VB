#!/usr/local/bin/python3

if __name__ == "__main__":
    
    while True:
        try:
            x =  int(input("Enter an integer: "))
            print ("you entered {} as an integer".format(x))
            break
        except ValueError:
             print("Enter an integer: ")
            
   
            

        
        
