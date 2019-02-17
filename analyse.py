#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
import argparse


def parser_assign():
	parser = argparse.ArgumentParser()
	parser.add_argument("file_name")   # name of the file specified in Dockerfile
	parser.add_argument("-header_name", "--header_name", default="default.txt", help="name of a headers file") #Optional header file name
	args = parser.parse_args()
	
	file_name = args.file_name
	if args.header_name:
		header_name = args.header_name
	
	return file_name, header_name

def read_data(file):
	'''Copying data from file to Data Frame'''

	names = ['ID', 'Diagnosis', 'radius_m', 'texture_m', 'perimeter_m', 'area_m', 'smothness_m', 'compactness_m', 'concavity_m', 'concave_points_m', 'symmetry_m', 'fractal_dim_m', 'radius_s', 'texture_s', 'perimeter_s', 'area_s', 'smothness_s', 'compactness_s', 'concavity_s', 'concave_points_s', 'symmetry_s', 'fractal_dim_s', 'radius_w', 'texture_w', 'perimeter_w', 'area_w', 'smothness_w', 'compactness_w', 'concavity_w', 'concave_points_w', 'symmetry_w', 'fractal_dim_w']
	
	#data = pd.read_csv(file, sep=',', names=names)
	data = pd.read_csv(file, sep='\s+|,', header=None)
	data.columns = names
	print(data)
	return data

def find_mean_std(P):
	'''Calculating mean and std for each of 30 features'''

	ave_feature = np.mean(P.iloc[:,2:],axis=0) 				
	std_feature = np.std(P.iloc[:,2:].astype(float),axis=0) 

	print('\n ave of each measurment:\n', ave_feature)
	print('\n std of each measurment:\n', std_feature)


#Assigning file names to local variables
data_file, header_file = parser_assign()
assert os.path.isfile(data_file), 'Not valid file'
print('File is assigned: ', data_file)
print('Header file is: ', header_file)


#Reading data from file to Data Frame
help(read_data)
data = read_data(data_file)


#Adding header


#Calculating summary statistics
help(find_mean_std)
find_mean_std(data)
""" except:
	print('something went wrong, please read the error: \n')
	print(e) """





