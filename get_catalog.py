import argparse
import numpy as np
import os
import urllib.request as urlib
import socket


def argument_parser():
    """
    Function that parses the arguments passed while running a script
    """
    result = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # path to the config file with parameters and information about the run
    result.add_argument("-c", dest="cutouts", type=str, default="catalogs.txt")
    result.add_argument("-d", dest="directory", type=str, default="catalogs.nosync")
    result.add_argument("-l", dest="layer", type=str, default="ls-dr9")
    result.add_argument("-m", dest="multithread", type=bool, default=False)

    return result


def download_catalog(cutout):
    ra, dec, size = cutout
    ra_min = ra - size
    ra_max = ra + size
    dec_min = dec - size
    dec_max = dec + size

    outname = f"/{ra}_{dec}.fits"
    if not os.path.isfile(outputs + outname):
        try:
            urlib.urlretrieve(
                url.format(args.layer, ra_min, ra_max, dec_min, dec_max),
                outputs + outname,
            )
        except Exception as e:
            print("\x1b[31m Catalog at [", ra, dec, "] timed out. :( \x1b[0m")
            return None

        print("\x1b[32m Catalog at [", ra, dec, "] has been downloaded. \x1b[0m")
    else:
        print("\x1b[33m Catalog at [", ra, dec, "] was already downloaded. \x1b[0m")


if __name__ == "__main__":
    # read in command line arguments
    args = argument_parser().parse_args()

    # define all locations and variables
    directory = os.getcwd()
    cutout_list = np.loadtxt(f"{directory}/{args.cutouts}")
    if len(cutout_list) == 0:
        raise ValueError("No cutouts found in config file.")

    if args.directory is None:
        outputs = directory
    else:
        outputs = f"{directory}/{args.directory}"

    url = "https://www.legacysurvey.org/viewer/{}/cat.fits?ralo={}&rahi={}&declo={}&dechi={}"

    socket.setdefaulttimeout(30)

    # loop through each cutout and download the data
    if not args.multithread:
        for cutout in cutout_list:
            download_catalog(cutout)
    else:
        from multiprocessing import Pool

        # from tqdm.contrib.concurrent import process_map
        # process_map(download_catalog, cutout_list)
        with Pool() as p:
            p.map(download_catalog, cutout_list)

    print("---------")
    print("Done.")
