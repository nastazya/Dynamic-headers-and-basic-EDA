#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
import argparse
import csv
import matplotlib.pyplot as plt
import string
import math
#import wx

def parser_assign():
	'''Setting up parser for the file name and header file name '''
	parser = argparse.ArgumentParser()
	parser.add_argument("file_name")   # name of the file specified in Dockerfile
	parser.add_argument("-d", "--header_name", default="no_file", help="name of a headers file") #Optional header file name
	args = parser.parse_args()
	f_name = args.file_name
	if args.header_name:
		h_name = args.header_name
	return f_name, h_name


def read_data(file,h_file):
	'''Copying data from file to Data Frame'''
	if file == 'wdbc.data':				# if this is breast cancer dataset
		names = ['ID', 'Diagnosis', 'radius_m', 'texture_m', 'perimeter_m', 'area_m', 'smothness_m', 'compactness_m', 'concavity_m', 'concave_points_m', 'symmetry_m', 'fractal_dim_m', 'radius_s', 'texture_s', 'perimeter_s', 'area_s', 'smothness_s', 'compactness_s', 'concavity_s', 'concave_points_s', 'symmetry_s', 'fractal_dim_s', 'radius_w', 'texture_w', 'perimeter_w', 'area_w', 'smothness_w', 'compactness_w', 'concavity_w', 'concave_points_w', 'symmetry_w', 'fractal_dim_w']
		data = pd.read_csv(file, sep=',', names=names)
		data.columns = names			# assigning feature names to the names of the columns
		data.index = data['ID']			# assigning ID column to the names of the rows
		del data['ID']					# removing ID column 
		#data = data.iloc[:10,:5]		# reducing data for testing putposes  
	
	elif check_header(file):			# if data has header
		print("\n Dataset has it's header \n")		
		data = pd.read_csv(file, sep='\s+|,')
	
	elif os.path.isfile(h_file):		# if header file was provided
		print("\n Dataset header will be generated from it's provided header file \n")	
		#filename='testcsv.csv'
		# Read column headers (to be variable naames)
		with open(h_file) as f:
			firstline = f.readline()                    # Read first line 
			firstline = firstline.replace("\n","")      # Remove new line characters
			firstline = firstline.replace(","," ") 		# Remove commas
			firstline = firstline.replace("  "," ")     # Remove spaces
			header = list(firstline.split(' '))			# Split string to a list
			
			data = pd.read_csv(file, sep='\s+|,', header=None)
			assert len(data.columns) == len(header), 'Number of columns is not equal to number of column names in header file.'
			data.columns = header
	else:								# if there is no header file we generate column names like A, B..., AA, BB...
		print("\n Dataset doesn't have nether header nor header file. It will be generated automatically \n")	
		data = pd.read_csv(file, sep='\s+|,', header=None, engine='python')
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
	'''Checking whether the data file contains header'''
	header_flag = csv.Sniffer().has_header(open(file).read(1024))
	print('result', header_flag)
	return header_flag


def find_mean_std(P):
	'''Calculating mean and std for each of 30 features'''
	ave_feature = np.mean(P) 		
	std_feature = np.std(P) 

	print('\n ave of each measurment:\n', ave_feature)
	print('\n std of each measurment:\n', std_feature)


def plot_histograms(df, columns, folder, name):
	'''Histogram all in one figure'''
	#app = wx.App(False)
	#width, height = wx.GetDisplaySize()		# Getting screen dimentions
	#plt.switch_backend('wxAgg')				# In order to maximize the plot later by using plt.get_current_fig_manager()

	l = len(columns)
	n_cols = math.ceil(math.sqrt(l))		#Calculating scaling for any number of features
	n_rows = math.ceil(l / n_cols)
	
	#fig=plt.figure(figsize=(width/100., height/100.), dpi=100)
	fig=plt.figure(figsize=(11, 6), dpi=100)
	for i, col_name in enumerate(columns):
		ax=fig.add_subplot(n_rows,n_cols,i+1)
		df[col_name].hist(bins=10,ax=ax)
		ax.set_title(col_name)
		#ax.set_xlabel('value')
		#ax.set_ylabel('number')
	fig.tight_layout() 
	plt.savefig("./{0}/all_hist_{1}.png".format(folder,name), bbox_inches='tight')
	#mng = plt.get_current_fig_manager()
	#mng.frame.Maximize(True)
	plt.show()

def plot_hist(features, name, folder):
	'''Histogram for each feature'''
	fig = plt.figure()
	plt.hist(features)
	plt.xlabel('value')
	plt.ylabel('number')
	plt.savefig("./{0}/{1}.png".format(folder,name), bbox_inches='tight')
	plt.close('all')


def plot_histograms_grouped(dff, columns, gr_feature, folder, name):
	'''Histogram: all features in one figure grouped by one element'''
	#app = wx.App(False)
	#width, height = wx.GetDisplaySize()		# Getting screen dimentions
	#plt.switch_backend('wxAgg')				# In order to maximize the plot later by using plt.get_current_fig_manager()

	df = dff								# Creating a copy of data to be able to manipulate it without changing the data
	l = len(columns)
	n_cols = math.ceil(math.sqrt(l))		# Calculating scaling for any number of features
	n_rows = math.ceil(l / n_cols)
	
	#fig=plt.figure(figsize=(width/100., height/100.), dpi=100)
	fig=plt.figure(figsize=(11, 6), dpi=100)
	df.index = np.arange(0,len(df))				# Setting indexes to integers (only needed if we use reset_index later)
	idx = 0
	for i, col_name in enumerate(columns):		# Going through all the features
		idx = idx+1
		if col_name != gr_feature:				# Avoiding a histogram of the grouping element
			ax=fig.add_subplot(n_rows,n_cols,idx)
			ax.set_title(col_name)
			#grouped = df.reset_index().pivot('index',gr_feature,col_name)	# This grouping is useful when we want to build histograms for each grouped item in the same time in different subplots. Here no need as I do it inside the for loop for each one on the same plot  
			grouped = df.pivot(columns='Diagnosis', values=col_name)
			for j, gr_feature_name in enumerate(grouped.columns):			# Going through the values of grouping feature (here malignant and benign)
				grouped[gr_feature_name].hist(alpha=0.5, label=gr_feature_name)
			plt.legend(loc='upper right')
		else: idx = idx-1
	fig.tight_layout() 
	plt.savefig("./{0}/all_hist_grouped_{1}.png".format(folder,name), bbox_inches='tight')
	#mng = plt.get_current_fig_manager()
	#mng.frame.Maximize(True)
	plt.show()


def plot_scatter(feature1, feature2, name1, name2, folder):
	'''Scatter for each pair of features'''
	fig = plt.figure()
	plt.xlabel(name1)
	plt.ylabel(name2)
	plt.scatter(feature1, feature2)
	plt.savefig(("./{0}/{1}-{2}.png".format(folder, name1, name2)), bbox_inches='tight')
	plt.close('all')
	

def plot_corr(data_frame, size, folder, file_n):
	''' Plotting correlations'''
	fig, ax = plt.subplots(figsize=(size, size))
	ax.matshow(data_frame)
	plt.xticks(range(len(data_frame.columns)), data_frame.columns)
	plt.yticks(range(len(data_frame.columns)), data_frame.columns)
	plt.savefig(("./{0}/{1}.png".format(folder,file_n)), bbox_inches='tight')
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
find_mean_std(data)


# Plotting histograms
if not os.path.exists('hist'):
	os.makedirs('hist')

if data_file == 'wdbc.data':
	print('\n Plotting all histograms into one figure')						#Plotting one histogram for all the features
	plot_histograms(data.iloc[:,1:11], data.iloc[:,1:11].columns, 'hist', data_file)
	print('\n Plotting all histograms into one figure grouped by diagnosis')#Plotting one histogram for all the features grouped by diagnosis
	plot_histograms_grouped(data.iloc[:,:11], data.iloc[:,:11].columns, 'Diagnosis', 'hist', data_file)
	for col_name in data.columns:											#Plotting a histogram for each feature 
		if col_name != 'Diagnosis':
			print('\n Plotting histogramme for ', col_name, ' into /hist/')
			plot_hist(data[col_name], col_name, 'hist')
else:
	print('\n Plotting all histograms into one figure')	#Plotting one histogram for all the features
	plot_histograms(data, data.columns, 'hist', data_file)
	for col_name in data.columns:						#Plotting a histogram for each feature
		print('\n Plotting histogramme for ', col_name, ' into /hist/')
		plot_hist(data[col_name], col_name, 'hist')


# Plotting scatter
if not os.path.exists('scatter'):
	os.makedirs('scatter')

if data_file == 'wdbc.data':			# Build the scatter only for mean of each feature (10 first columns out of 30)
	for i in range(1, 11):
		j = 1
		for j in range((i+j),11):
			col_name1 = data.iloc[:,i].name
			col_name2 = data.iloc[:,j].name
			print('\n Plotting scatter for ', col_name1, col_name2, ' into /scatter/')
			plot_scatter(data[col_name1], data[col_name2], col_name1, col_name2, 'scatter')
else:
	for i in range(len(data.iloc[0])):
		j = 1
		for j in range((i+j),len(data.iloc[0])):
			col_name1 = data.iloc[:,i].name
			col_name2 = data.iloc[:,j].name
			print('\n Plotting scatter for ', col_name1, col_name2, ' into /scatter/')
			plot_scatter(data[col_name1], data[col_name2], col_name1, col_name2, 'scatter')


# Plotting correlations heatmap
if data_file == 'wdbc.data':
	print('\n Plotting correlation hitmap into /corr/ ')
	if not os.path.exists('corr'):
		os.makedirs('corr')
	data_features =data.iloc[:,1:11]
	plot_corr(data_features.corr(), 10, 'corr', data_file)	# Calculating correlation of 10 features and send them to plot
else:
	print('\n Plotting correlation hitmap into /corr/ ')
	if not os.path.exists('corr'):
		os.makedirs('corr')
	plot_corr(data.corr(), 10, 'corr', data_file)			# Calculating correlation and send them to plot
	
	
	



