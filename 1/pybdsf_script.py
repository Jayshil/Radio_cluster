import bdsf

from numpy import *
import glob
#import pyfits as fits
from astropy.io import fits

img=glob.glob('*_NVSS.FITS')

#save_file='NVSS.sav'
for inp_img in img:
  Img=bdsf.process_image(inp_img,  beam=(0.0125,0.0125,0), frequency=1400e6, quiet=True,rms_box=(100,50),thresh_isl=1,thresh_pix=1)
  Img.export_image(img_type='gaus_resid',clobber=True,pad_image=True)

