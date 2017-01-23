#!/usr/local/bin/python3


number_of_cats = 100
cats_with_hats = {}

# put hat on every cat
for idx in range(1, number_of_cats+1):
    cat = "cat{}".format(idx)
    cats_with_hats[cat] = True

#continue on with second cat and go on

for next_cat_idx in range(2, number_of_cats + 1):
    for next_cat in range(next_cat_idx, number_of_cats + 1, next_cat_idx):
        cat = "cat{}".format(next_cat_idx)
        if cats_with_hats[cat] == True:
            cats_with_hats[cat] = False
        else:
            cats_with_hats[cat] = True

print (cats_with_hats['cat1'])

   
