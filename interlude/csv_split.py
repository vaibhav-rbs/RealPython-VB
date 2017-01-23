#!/usr/local/bin/python3
import csv
import os
import operator
import argparse



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type=str,
        default = os.getcwd(),
        help="input CSV file")
    parser.add_argument("-o", type=str,
        help="specify outfile")
    parser.add_argument("-r", type=int,
        help="specify row cutout")
    args = parser.parse_args()
    return (args.i, args.o, args.r)

def validate_file(file_name):
   try:
        with open(file_name, "rt") as f:
            reader = csv.reader(f)
            data = list(reader)
            row_count = len(data)
   except IOError:
        print ("Error: can't find file or read data")
        return False
   else:
       return (True,row_count, data)
 
def split_files(row_count , data ,thresh_hold, name_of_outfile):
    k = 0 
    for i in range(0, row_count, thresh_hold):
        outfile = name_of_outfile
        k = k + 1
        outfile = outfile + str(k)
        with open(outfile, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            j = i
            while j < i + thresh_hold:
                try:
                    spamwriter.writerow(data[j])
                    j = j +1
                except IndexError:
                    print ("EOF reached exiting")
                    break

    

if __name__ == "__main__":
    file_status = validate_file(get_args()[0])[0]
    file_lc = validate_file(get_args()[0])[1]
    file_data = validate_file(get_args()[0])[2]
    split_files(file_lc, file_data, get_args()[2], get_args()[1])
        
