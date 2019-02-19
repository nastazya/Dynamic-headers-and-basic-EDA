#!/usr/bin/env python



import os
import numpy as np
import pandas as pd
import argparse
import csv
import matplotlib.pyplot as plt
import string

def parser_assign():
	'''Setting up parser for the file name and header file name '''

	parser = argparse.ArgumentParser()
	parser.add_argument("file_name")   # name of the file specified in Dockerfile
	parser.add_argument("-header_name", "--header_name", default="no_file", help="name of a headers file") #Optional header file name
	args = parser.parse_args()
	
	file_name = args.file_name
	if args.header_name:
		header_name = args.header_name
	
	return file_name, header_name


def read_data(file,h_file):
	'''Copying data from file to Data Frame'''

	if file == 'wdbc.data':				# if this is breast cancer dataset
		names = ['ID', 'Diagnosis', 'radius_m', 'texture_m', 'perimeter_m', 'area_m', 'smothness_m', 'compactness_m', 'concavity_m', 'concave_points_m', 'symmetry_m', 'fractal_dim_m', 'radius_s', 'texture_s', 'perimeter_s', 'area_s', 'smothness_s', 'compactness_s', 'concavity_s', 'concave_points_s', 'symmetry_s', 'fractal_dim_s', 'radius_w', 'texture_w', 'perimeter_w', 'area_w', 'smothness_w', 'compactness_w', 'concavity_w', 'concave_points_w', 'symmetry_w', 'fractal_dim_w']
		data = pd.read_csv(file, sep=',', names=names)
		data.columns = names			# assigning feature names to the names of the columns
		data.index = data['ID']			# assigning ID column to the names of the rows
		del data['ID']					# removing ID column 
		#data = data.iloc[:10,:5]		# reducing data for testing putposes  
	
	elif check_header(file):			# check if data has header
		print("\n Dataset has it's header \n")		
		data = pd.read_csv(file, sep='\s+|,')
	
	elif os.path.isfile(h_file):		#if header file was provided
		print("\n Dataset header will be generated from it's provided header file \n")	
		'''		
		Add reading header from file
		'''
	else:								# if there is no header file we generate column names like A, B..., AA, BB...
		print("\n Dataset doesn't have nether header nor header file. It will be generated automatically \n")	
		data = pd.read_csv(file, sep='\s+|,', header=None)
		s = list(string.ascii_uppercase)
		col_number = len(data.columns)
		print(col_number)
		header = s
		if col_number > len(s):			# if number of columns is greater then 26 
			if col_number % 26 != 0:
				n = (col_number // 26) + 1
			else: n = (col_number // 26)
			print(n)
			
			for i in range(2, n+1):
				for j in range(len(s)):
					header += [s[j]*i]
		#print('auto-header: ',header)
		#print(header[:len(data.columns)])

		data.columns = header[:len(data.columns)]
	return data


def check_header(file):
	'''Checking wether the data file contains header'''
	return csv.Sniffer().has_header(open(file).read(3000))


def find_mean_std(P):
	'''Calculating mean and std for each of 30 features'''

	ave_feature = np.mean(P.iloc[:,2:],axis=0) 				
	std_feature = np.std(P.iloc[:,2:].astype(float),axis=0) 

	print('\n ave of each measurment:\n', ave_feature)
	print('\n std of each measurment:\n', std_feature)


def plot_hist(features, name, folder):
	'''Histogram for each feature'''

	fig = plt.figure()
	plt.hist(features)
	plt.savefig((f"./{folder}/{name}.pdf"), bbox_inches='tight')
	plt.close('all')
	
	
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# Assigning file names to local variables
data_file, header_file = parser_assign()
assert os.path.isfile(data_file), '\n Not valid file!!!'




# Reading data from file to Data Frame
data = read_data(data_file, header_file)
print(data)


# Calculating summary statistics
'''find_mean_std(data)'''


#Plotting histograms
'''if not os.path.exists('hist'):
	os.makedirs('hist')

for col_name in data.columns:
	#print(data[col_name])
	print('\n Plotting histogramme for ', col_name)
	plot_hist(data[col_name], col_name, 'hist')'''





