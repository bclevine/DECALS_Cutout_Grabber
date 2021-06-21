import argparse
import numpy as np
import os
import urllib.request as urlib

def argument_parser():
    '''
    Function that parses the arguments passed while running a script

	fits : str, the multi extension fits file outputted by galfit
	for_cutout: str, True of False
    '''
    result = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # path to the config file with parameters and information about the run
    result.add_argument('-c', dest='cutouts', type=str, default="cutouts.txt") 
    result.add_argument('-d', dest='directory', type=str, default=None) 
    result.add_argument('-l', dest='layer', type=str, default="ls-dr9")
    result.add_argument('-s', dest='scale', type=float, default=0.262)
    result.add_argument('-t', dest='type', type=str, default="fits")
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

    if args.type == 'fits':
        url = 'https://www.legacysurvey.org/viewer/fits-cutout?ra={}&dec={}&size={}&layer={}&pixscale={}&bands=grz'
    elif args.type == 'jpeg':
        url = 'https://www.legacysurvey.org/viewer/jpeg-cutout?ra={}&dec={}&size={}&layer={}&pixscale={}&bands=grz'
    else:
        raise ValueError("Type must be either 'fits' (default) or 'jpeg'.")

    # loop through each cutout and download the data
    for cutout in cutout_list:
        ra, dec, size = cutout
        outname = '/'+str(ra)+'_'+str(dec)+'.'+args.type
        urlib.urlretrieve(url.format(ra, dec, int(size), args.layer, args.scale),outputs+outname)
        print('Cutout at [', ra, dec, '] has been downloaded.')
    
    print('---------')
    print('Done.')