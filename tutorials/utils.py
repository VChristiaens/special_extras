#! /usr/bin/env python

"""
Utility functions to read external formatted files (filters and models).
"""

__author__ = 'Valentin Christiaens'
__all__ = ['bts_reader',
           'filter_reader',
           'tmp_reader']

import numpy as np
import pandas as pd
from special.utils_spec import convert_F_units, nrefrac
from special.fits import open_fits

def bts_reader(params, ground=True):
    # snippet to read BT-SETTL fits files and return a tuple: lbda (mu), spec (SI)
    mod_units = 'cgs' # careful: input in cgs
    mod_path = '../static/btsettl15_models/'
    filename = mod_path+'btsettl15_t{:.0f}_g{:.1f}0_z-0.00_SED.txt'.format(params[0],params[1])        
    lbda = []
    flux = []
    f=open(filename,"r")
    lines=f.readlines()
    for i, x in enumerate(lines):
        if i>0:
            lbda.append(float(x.split('\t')[0]))
            flux.append(float(x.split('\t')[1]))
    f.close() 
    
    # Correct for atmospheric refraction
    flux = np.array(flux) 
    lbda = np.array(lbda)
    if ground:
        # truncate at 100nm (no transmission)
        flux = flux[np.where(lbda>0.2)]
        lbda = lbda[np.where(lbda>0.2)]
        # then correct for the shift in wavelength due to atm. refraction
        nref = nrefrac(lbda*1e4)
        lbda = lbda/(1+(nref*1e-6))
    
    #conversion from ergs/s/cm2/um to W/m2/um
    flux = convert_F_units(flux, lbda, in_unit=mod_units, out_unit='si') 
    
    return lbda, flux


def filter_reader(filename):
    # snippet to read filter files and return a tuple: lbda (mu), transmission
    filter_path = "../static/filters/"
    filt_table = pd.read_csv(filter_path+filename, sep=' ', header=0, 
                             skipinitialspace=True)
    keys = filt_table.keys()
    lbda_filt = np.array(filt_table[keys[0]])
    if lbda_filt.dtype == 'O':
        filt_table = pd.read_csv(filter_path+filename, sep='\t', header=0, 
                                 skipinitialspace=True)
        keys = filt_table.keys()
        lbda_filt = np.array(filt_table[keys[0]])
    elif lbda_filt.dtype == 'int32' or lbda_filt.dtype == 'int64': 
        lbda_filt = np.array(filt_table[keys[0]], dtype='float64')
    if '(AA)' in keys[0]:
        lbda_filt /=10000
    elif '(mu)' in keys[0]:
        pass
    elif '(nm)' in keys[0]:
        lbda_filt /=1000
    else:
        raise ValueError('Wavelength unit not recognised in filter file')
    trans = np.array(filt_table[keys[1]])
    return lbda_filt, trans 
    
def tmp_reader(tmp_name, verbose=False):
    inpath_tmp=  '../static/MSL/'
    if verbose:
        print("opening {}".format(tmp_name))
    spec_model = open_fits(inpath_tmp+tmp_name, verbose=False,
                           output_verify='ignore')
    lbda_model = spec_model[0]
    flux_model = spec_model[1]
    flux_model_err = spec_model[2]
    return lbda_model, flux_model, flux_model_err