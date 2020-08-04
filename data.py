import numpy as np

f1 = open('list_rossetti.dat','w')

while a = True:
    name = input("Enter the name of cluster: ")
    ra = input("Enter the RA of cluster: ")
    dec = input("Enter the DEC of cluster: ")
    f1.write(name + '\t')
    f1.write(ra + '\t')
    f1.write(dec + '\n')
    b = input('Do you want to continue (y/n)? ')
    if b == 'y':
        a = True
    else:
        a = False

f1.close()
