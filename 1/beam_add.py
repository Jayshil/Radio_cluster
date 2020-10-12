from numpy import *
import glob
#from astropy.io import fits
import pyfits as fits
img=glob.glob('*FITS')

for i in range(len(img)):
 #  data=fits.getdata(img[i])
 #  hdulist = fits.open(img[i])
 #  hdr=hdulist[0].header
 #  hdr.insert(5,('BEAMMAJOR','0.0125'))
 #  hdr.insert(6,('BEAMMINOR','0.0125'))
 #  hdr.insert(7,('BEAMPA','0'))
 #  hdr.insert(8,('FREQUENCY','1400e6'))
 #  fits.writeto(img[i],data,hdr,overwrite=True)
   
   print 'fparkey 0.0125 "'+str(img[i])+'[0]" bmaj add=yes'
   print 'fparkey 0.0125 "'+str(img[i])+'[0]" bmin add=yes'
   print 'fparkey 0.0 "'+str(img[i])+'[0]" bpa add=yes'
   print 'fparkey 1.4e6 "'+str(img[i])+'[0]" frequency add=yes'
