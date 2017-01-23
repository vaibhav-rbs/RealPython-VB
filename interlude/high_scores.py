#!/usr/local/bin/python3
import csv
import os
import operator

my_path ="/Users/vaibhavchauhan/RealPython/book1-exercises/chp09/practice_files"

my_file = "scores.csv"
score_dict = {}
with open(os.path.join(my_path, my_file), "r") as csv_file:
    my_file_reader = csv.reader(csv_file)
    next(my_file_reader)
    for name,score in my_file_reader:
        if name in score_dict:
            if score_dict[name] > score:
                score_dict[name] = score
        else:
            score_dict[name] = score
sorted_score_list = sorted(score_dict.items(), key=operator.itemgetter(0))

for items in sorted_score_list:
    print (items[0], items[1])     
