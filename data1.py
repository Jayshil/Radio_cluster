import numpy as np
from astropy import coordinates as coor
from astropy import units as u

f1 = open('list_lovisari.dat','w')

a = True

while a==True:
    name = input("Enter the name of the cluster: ")
    ra_g = name[1:7]
    dec_g = name[7:]
    c = coor.SkyCoord(float(ra_g), float(dec_g), frame='galactic', unit='deg')
    d = c.icrs
    ra1 = d.ra.degree
    dec1 = d.dec.degree
    f1.write(name + '\t')
    f1.write(format(ra1, '.4f') + '\t')
    f1.write(format(dec1, '.4f') + '\n')
    xx = input('Do you want to continue (y/n)? ')
    if xx == 'y':
        a = True
    else:
        a = False

f1.close()
