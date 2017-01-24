#!/usr/local/bin/python3
INPUT_TEXT="Hi, my name is Sylvestor(Software Developer in (Cisco Systems)). I work with DevX(CSG)."


list_postional = []
out_list = []
for idx in range(len(INPUT_TEXT)):
    if INPUT_TEXT[idx] == "(":
        list_postional.append(idx)
    if INPUT_TEXT[idx] == ")":
        out_list.append((list_postional.pop(),idx))
print (out_list)
