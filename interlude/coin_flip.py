#!/usr/local/bin/python3

from random import randint

head = tail = False

trials = 10000
for trial in range(trials):
    flip = 0
    first_out_come = randint(0,1)
    if first_out_come == 0:
        head = True
    else:
        tail = True
    flip = flip + 1

    while head:
        second_out_come = randint(0,1)
        if second_out_come != 0:
            head = False
        flip = flip + 1
    
    while tail:
        second_out_come = randint(0,1)
        if second_out_come != 1:
            tail = False
        flip = flip + 1
print (flip/trials)
        

   
