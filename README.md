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
_4.1 check if the dataset contains a header_
     ```
     
     ```
4.2 If the file contains the header
```

```
4.3 If there is no header:
  * if file_name is my chosen dataset:
  ```
	header ← constant list on names for my chosen dataset
	data.columns ← header 						
  ```
  * for all other datasets:
    - if header_name is a file (we assign a header file):
    ```
  	read one line from header file, change it to be able to assign it to a list variable
  	header ← "clean" string of names from file transformed to a list
  	obligatory assert to check for equal nubmer of dataset columns and header items (len(header) == len(data[0]))
  	data.columns ← header 						
    ```
    - if we didn't assign a header file (else): assign column names automatically:
      * create a string of alphabetical chars:
      ```
      s ← sring.ascii_uppercase #create a 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'		 # 26 characters   
      ```
      * calculate a quantity of strings needed to name the columns to be able to generate a list with non-repetitive chars in a loop like AA or AAA to name all the columns
      ```
      n ← (col_number // 26) + (col_number % 26)
      ```
      * generate a double-loop to create a header and add it to dataset:
      ```
    	header ← []
        for i in range(1, n+1)
            for j in s
                header += s[j]*i
        data.columns ← header[:len(data[0])] 	#assign the number of names equal to number of dataset columns
      ```
	
**5) Compute summary statistics:**
* Mean: `np.mean(data)`
* Standart deviation: `np.std(data)`
* Median: `np.median(data)`
	
**6) Visualize data**
* Show a hystogramme for one feature at a time and write each image into a file:
```
	for i in range(len(data[0])):
            pyplot.plot(data[:,i]))
```
* Compare 2 features at a time write each image into a file:
```
	j = 0
        for i in range(len(data[0])):
            for j in range((i+j),len(data[0])):
                pyplot.skatter(data[:,i], data[:,j]))
```
				
