from __future__ import division, print_function
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser
#import dear_spectrum as ds

if __name__ == '__main__':

    parser = ArgumentParser(description="Histogram plot attribues.")

    parser.add_argument("data_filepath", type=str,
                        help = "The location of the data file.")

    args = parser.parse_args()

    # data = ds.utils.parse_data(data_filepath = args.data_filepath,
    #                            columns = ['RV_ADOP','FEH_ADOP','DIST_ADOP'])
    
    stars_data_hdulist = fits.open(args.data_filepath, memmap=True)
    stars_table = stars_data_hdulist[1]

    all_spec_types = set(stars_table.data['SPECTYPE_HAMMER'])
    print("Spectral Types: ")
    print(all_spec_types)

    radial_velocity = stars_table.data['RV_ADOP']
    heliocentric_distance = stars_table.data['DIST_ADOP']
    metallicity = stars_table.data['FEH_ADOP']

    good_inds = ((radial_velocity != -9999) &
                 (heliocentric_distance != -9999) &
                 (metallicity != -9999))

    radial_velocity = radial_velocity[good_inds]
    heliocentric_distance = heliocentric_distance[good_inds]
    metallicity = metallicity[good_inds]

    fig, axes = plt.subplots(1,3)
    axes[0].hist(radial_velocity,bins=30)
    axes[0].set_xlabel("Radial Velocity")
    axes[1].hist(heliocentric_distance,range=[0,100],bins=30)
    axes[1].set_xlabel("Heliocentric Distance")
    axes[2].hist(metallicity,bins=30)
    axes[2].set_xlabel("FeH")
    plt.tight_layout()
    fig.savefig("block_1.pdf")
    


    

    
    

    
    
    
    


