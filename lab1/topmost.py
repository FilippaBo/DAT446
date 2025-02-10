import wordfreq
import sys

#obs se till att close alltid finns
inp_file = open(sys.argv[1]) # för mac
#inp_file = open(sys.argv[1], encoding="utf-8")   för windows

list_with_element=[]
for line in inp_file:
    list_with_element.append(line.strip())
    


inp_file.close()

print (list_with_element)