from random import randint
try = 0

while try <= 10000:
    outcome = randint(1,6)
    sum_of_outcome = sum_of_outcome + outcome
    try = try + 1
average_out_come = sum_of_outcome//10000
print (average_out_come)
