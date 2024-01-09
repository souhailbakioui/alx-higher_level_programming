#!/usr/bin/python3
def no_c(my_string):
    listchar=list(my_string)
    for caracter in listchar:
        if caracter=='c' or caracter =='C':
            listchar.remove(caracter)
    return("".join(listchar))
