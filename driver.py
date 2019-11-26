import cdms2, MV2
import cdtime
import numpy as np
import numpy.ma as ma
import glob
import matplotlib.pyplot as plt
import os
import scipy.io
from convection_onset_statistics import convection_onset_statistics


#Read in model data

models = ['CNRM-CM5','CanAM4','bcc-csm1-1']
vas = ['pr','prw']
basedir='/Users/zhang40/Documents/cfSite/' #data on local computer
output_path = os.path.join(basedir,'output')
sites = 'Nauru'

for imod in range(len(models)):
    #Read in Precipitation 
    filename = glob.glob(os.path.join(basedir+'*'+vas[0]+'_cfSites_'+models[imod]+'*'))[0]
    f_in=cdms2.open(filename)
    pr=f_in(vas[0],time=('1979-01-01','1979-12-31')) #Read in the variable 

    #Read in CWV
    filename = glob.glob(os.path.join(basedir+'*'+vas[1]+'_cfSites_'+models[imod]+'*'))[0]
    f_in=cdms2.open(filename)
    prw=f_in(vas[1],time=('1979-01-01','1979-12-31')) 

    #Nauru ARM site 31
    pr_site=pr[:,30]*3600.           #'kg m-2 s-1' to 'mm/hr'
    prw_site=prw[:,30]               #'kg m-2' to 'mm'

   #Call calculation and plotting function 
   convection_onset_statistics(prw_site, pr_site,models[imod], output_path, sites)
