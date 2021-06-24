import argparse
import numpy as np
import os
import urllib.request as urlib

def argument_parser():
    '''
    Function that parses the arguments passed while running a script
    '''
    result = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # path to the config file with parameters and information about the run
    result.add_argument('-c', dest='cutouts', type=str, default="catalogs.txt") 
    result.add_argument('-d', dest='directory', type=str, default="catalogs") 
    result.add_argument('-l', dest='layer', type=str, default="ls-dr9")

    return result


if __name__ == '__main__': 
    
    # read in command line arguments
    args = argument_parser().parse_args()

    # define all locations and variables
    directory = os.getcwd()
    cutout_list = np.loadtxt(directory+'/'+args.cutouts)
    if len(cutout_list) == 0:
        raise ValueError("No cutouts found in config file.")

    if args.directory == None:
        outputs = directory
    else:
        outputs = directory+'/'+args.directory

    url = 'https://www.legacysurvey.org/viewer/{}/cat.fits?ralo={}&rahi={}&declo={}&dechi={}'

    # loop through each cutout and download the data
    for cutout in cutout_list:
        ra, dec, size = cutout
        ra_min = ra-size; ra_max = ra+size
        dec_min = dec-size; dec_max = dec+size

        outname = '/'+str(ra)+'_'+str(dec)+'.fits'
        urlib.urlretrieve(url.format(args.layer, ra_min, ra_max, dec_min, dec_max),outputs+outname)
        print('Catalog at [', ra, dec, '] has been downloaded.')
    
    print('---------')
    print('Done.')