#!/usr/bin/env python3
'''
TODO: write a doc string
'''

# Loading recommended packages
import os
import sys
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt

#TODO: check the correct number of arguments were provide and exit the script if they were not

#TODO: Read in the normalized matrix for the GM12878 and K562 cells

#TODO: Read in the list of genomic loci (genomic_bins.tsv) and the positional information of the TAD boundaries.

#TODO: subset the genomic location of each TAD

#TODO: find the indices of the start and end locations of the TAD boundaries within the list of genomic locations.


## Part 1

#Complete the function plot_hic_map(). This function should take as input the matrix to plot, the TAD boundary indices to plot, the title, the file name, and the percentile cutoff for the maximum intensity (default to 95th percentile)

#TODO: write a function plot_hic_map() that will plot a heatmap of the contact matrices. 
# As part of this function you should define the maximum intensity of the heatmap based on the n'th percentile of the data (do not harcode this). 
# Identify the value from the input matrix that is the n'th percentile (n here is one of your inputs to the function)
# Plot a heatmap of the matrix (use a colormap in this plot. one way to fine control the colormap is the use the LinearSegmentedColormap.from_list() method to generate the colormap used in the plot). 
# The minimum value should be 0 and the maximum should be set to the value of the nth percentile you generated.
# add lines to the heatmap where the TAD boundaries are if the TADs are present in the heatmap
# add a title


## Part 2

#TODO: plot the GM matrix as a heatmap using the plot_hic_map() function
#TODO: plot the K562 matrix as a heatmap using the plot_hic_map() function


## Part 3

#TODO: define a function block_contact_freq() that will subset the original matrix provided to it based on a list of index values provided to it. 
# As input this function should accept an input matrix and index values which may be are the start and end locations of a TAD in that matrix
# The function should first generate a copy of the original matrix to work from (if using numpy we recommend np.copy() and if using pandas we recommend <variable_for_your_dataframe.copy()) <- will cover why in lecture
# The function should then slice the copied matrix at the positions indicated in the input list. 
# Throw away the diagonal since this represents self-interactions within bins and is generally uninformative (set the diagoal values of the matrix to zero)
# calculate either the intra TAD interaction frequency if just a single TAD is in teh coordinates or the inter TAD interaction frequency if more than one TAD is present
# intra TAD interaction frequency formula: (sum_of_everything_in_subset_matrix)/(number_of_tads_in_original_matrix)
# inter TAD interaction frequency formula: (sum_of_everything_in_subset_matrix)/(number_of_tads_in_original_matrix) - (sum of each TAD's intra TAD interaction frequency)
# return the intra or inter TAD interaction frequncy


## Part 4

#TODO: use the block_contact_freq() function to calculate the intra-TAD interaction frequency for each TAD and the inter-TAD interaction frequency for GM12878 cells

#TODO: use the function to calculate the intra-TAD interaction frequency for each TAD and the inter-TAD interaction frequency for K562 cells

#TODO: convert all interaction frequencies into percents for each cell line. (if you are using pandas to store the interaction frequencies then make a copy of the dataframe you are using before doing so)

#TODO: Write all interaction frequencies intra and inter to the output file (cell_interaction_frequencies.txt). Then write each of the percents to the same outputfile.
