## Instructions for running analyse.py from bash

**1) Copy to local repository:**
- analyse.py 
- test_noheader.txt and header_5.txt to test adding the header from a file
- any data file you want to test

**2) Run the script in this format: **
```
python analyse.py <data_file> <-d header_file>
```
where  `<data_file>` is mandatory and `<-d header_file>` is optional

**3) Observe resulting plots in the following folders:**
- hist 		- for histograms
- scatter 	- for scatter plots
- corr		- for correlations heatmap


## Pseudocode
**1) Download the data to local directory:**

**2) Set up dynamic file input using:**
```
	parser.add_argument("file_name")    						#positional argument
	parser.add_argument("-header_name", "--header_name", default="default.txt") 	#optional header file name
	file_name = args.file_name
	if args.header_name:
	    header_name = args.header_name
```
**3) Load the data into the DataFrame:**
```
	data = pd.read_csv(file_name, sep='\s+|,', header=None)
```
**4) Set up the header dynamically:**
```
```
_4.1. If file_name is my chosen dataset:_
```
	header ← constant list on names for my chosen dataset
	data.columns ← header 						
```
_4.2. For all other datasets:_
- Check whether the dataset contains a header
```
	csv.Sniffer().has_header(open(file).read(2000))
```
- If data contains the header
```
	data ← pd.read_csv(file, sep='\s+|,')	#Header is assigned automaticly
```
- If there is no header:
  * If header_name is a file (we assigned a header file):
  ```
  	read one line from header file, change it to be able to assign it to a list variable
  	header ← "clean" string of names from file transformed to a list
  	obligatory assert to check for equal nubmer of dataset columns and header items (len(header) == len(data[0]))
  	data.columns ← header 
  ```
  * If we didn't assign a header file (else): assign column names automatically:
    - create a string of alphabetical chars:
    ```
    	s ← list(string.ascii_uppercase) 		# create a list of 26 unique characters
    ```
    - calculate a quantity of strings needed to name the columns to be able to generate a list with non-repetitive chars in a loop like AA or AAA to name all the columns
    ```
	 if col_number > len(s):				# if number of columns is bigger then our list of characters
	    if col_number % 26 != 0:
		n ← col_number // 26 + 1
	    else: n ← col_number // 26	
    ```
    - generate a double-loop to create a header and add it to dataset:
    ```
	header ← s					# assign a list of characters to a header list
	if col_number > len(s):
	    for i in range(2, n+1):
	    	for j in range(len(s)):
		    header += [s[j]*i]
        data.columns ← header[:len(data.columns)] 	#assign the number of names equal to number of dataset columns
    ```

**5) Compute summary statistics:**
* Mean: `np.mean(data)`
* Standart deviation: `np.std(data)`
* Median: `np.median(data)`
	
**6) Visualize data**
* Show a hystogramme for one all the features in one figure and show it:
```	
	fig=plt.figure()
	for i, col_name in enumerate(data.columns):
		ax=fig.add_subplot(n_rows,n_cols,i+1)
		data[col_name].hist(bins=10,ax=ax)
		ax.set_title(col_name)
	fig.tight_layout() 
	plt.show()	
```
* Show a hystogramme for one feature at a time and write each image into a file:
```	
	fig = plt.figure()
	plt.hist(features)				#build a histogram for each column
	plt.savefig(f"./{folder}/{name}.pdf")		#save to the custom dir each plot as .pdf with the name of the column
	plt.close('all')
	
```
* Compare 2 features at a time write each image into a file:
```
	for i in range(len(data[0])):
	    j = 1
            for j in range((i+j),len(data[0])):
                plt.skatter(data[:,i], data[:,j]))
		plt.savefig((f"./{folder}/{name1}-{name2}.pdf"), bbox_inches='tight') # folder = given folder name; name1, name2 - names of the columns
```
* Build correlation heatmap and write in into a file:
```
	data_frame = data.corr()			# Calculates correlations
	fig, ax = plt.subplots(figsize=(size, size))
	ax.matshow(data_frame)
	plt.xticks(range(len(data_frame.columns)), data_frame.columns)
	plt.yticks(range(len(data_frame.columns)), data_frame.columns)
	plt.savefig((f"./{folder}/corr.png"), bbox_inches='tight')
	plt.close('all')
```
				
