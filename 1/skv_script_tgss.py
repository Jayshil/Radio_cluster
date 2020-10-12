#!/usr/bin/python

#Python script for downloading 2MASS images using the Skyview
#batch scripts see -- http://skyview.gsfc.nasa.gov

#The skvbatch_wget script is used here.
#- The input catalog is a csv file with 3 columns that must be
#  the ra(decimal degrees), dec(decimal degrees), ObjID
#- 900x900 pixel size is specified
#- images are saved in directories named with the  ObjID
#  with each directory containing files named with the band:
#  J.fits, H.fits and K.fits

#To run the script:
#python skv_script.py radecobjid.csv
#

import os, sys
import commands


# Read input table (CSV)
import csv
import numpy as np

file1='ra_dec_deg.txt'
#data=(np.loadtxt(file))
ra, dec = np.loadtxt(file1, usecols=(1,2), dtype=str, unpack=True)
#reader=csv.reader(open(file, "rb"))
#ra=data[:,0]
#dec=data[:,1]
#objid=[]
#for row in reader:
#   ra.append(float(row[0]))
#   dec.append(float(row[1]))
   #objid.append(str(row[2]))

#print ra,dec,objid
#bands=['J', 'H', 'K']

# Loop for each object
for i in range(len(ra)):
  # Output dir is the object id
  #output_dir = objid[i]
  # Create directory if it does not exist
  #if not os.access(output_dir, os.R_OK): os.mkdir(output_dir)
  # Loop for each image
#  for band in bands:
  command = 'perl skvbatch_wget file='+str(ra[i])+'_'+str(dec[i])+'_TGSS.FITS position='+str(ra[i])+','+str(dec[i])+" Survey='tgss"+"' " 
  print command
  res=commands.getoutput(command)

#for i in range(len(ra)):
  # Output dir is the object id
#  output_dir = objid[i]
  # Create directory if it does not exist
#  if not os.access(output_dir, os.R_OK): os.mkdir(output_dir)
  # Loop for each image
#  for band in bands:
#  command = 'perl skvbatch_wget file='+objid[i]+'/'+objid[i]+'_sumss.fits position='+str(ra[i])+','+str(dec[i])+" Survey='sumss"+"' " 
#  print command
#  res=commands.getoutput(command)

#for i in range(len(ra)):
  # Output dir is the object id
#  output_dir = objid[i]
  # Create directory if it does not exist
#  if not os.access(output_dir, os.R_OK): os.mkdir(output_dir)
  # Loop for each image
#  for band in bands:
#  command = 'perl skvbatch_wget file='+objid[i]+'/'+objid[i]+'_HRI.fits position='+str(ra[i])+','+str(dec[i])+" Survey='HRI"+"' " 
#  print command
#  res=commands.getoutput(command)

#for i in range(len(ra)):
  # Output dir is the object id
#  output_dir = objid[i]
  # Create directory if it does not exist
#  if not os.access(output_dir, os.R_OK): os.mkdir(output_dir)
  # Loop for each image
#  for band in bands:
#  command = 'perl skvbatch_wget file='+objid[i]+'/'+objid[i]+'_first.fits position='+str(ra[i])+','+str(dec[i])+" Survey='first"+"' " 
#  print command
#  res=commands.getoutput(command)


#for i in range(len(ra)):
  # Output dir is the object id
#  output_dir = objid[i]
  # Create directory if it does not exist
#  if not os.access(output_dir, os.R_OK): os.mkdir(output_dir)
  # Loop for each image
#  for band in bands:
#  command = 'perl skvbatch_wget file='+objid[i]+'/'+objid[i]+'_dss.fits position='+str(ra[i])+','+str(dec[i])+" Survey='dss"+"' " 
#  print command
#  res=commands.getoutput(command)





#  for band in bands:
#     command = './skvbatch_wget file='+objid[i]+'/'+ band + '.gif position='+str(ra[i])+','+str(dec[i])+" Survey='SDSS"+band+"' pixels=900 Deedger=skyview.process.deedger.ImageMedian" 
#      print command
#      res=commands.getoutput(command)





