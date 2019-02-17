# class5_homework

*1) Download the data to local directory:*

*2) Set up dynamic file input using `argparse`:*
	`parser.add_argument("file_name")   # positional argument`
	  `parser.add_argument("-header_name", "--header_name", default="default.txt") # optional header file name`
	- `file_name = args.file_name`
	  `if args.header_name:`
	- `header_name = args.header_name`
3) Load the data into the DataFrame:
	- `data = pd.read_csv(file_name, sep='\s+|,', header=None)`

4) Add header dynamically:
	- `if file_name == 'wdbc.data':`
	  	`header = my custom string for my chosen dataset`
        	`data.columns = header #will assign header without changing the dimentions`
	- `for all other datasets:`
	  	- `if header_name is a file:`
			`read one line from header_name, change it to be able to assign it to a list variable`
            		`header = "clean" string of names from file`
            		`obligatory assert to check len(header) == len(data[0])`
            		`data.columns = header #will assign header without changing the dimentions`
		- `else(if we didn't assign a header file):`
			`assign column names automatically:`
            		`s = sring.ascii_uppercase #create a 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 26 characters`
            		`calculate a var n for the loop to be able to generate a list with non-repetitive chars like AA or AAA to name 					all the columns`
            		`if col_number % 26 != 0:`
                		`n = col_number // 26 + 1`
            		`else:`
                		`n = col_number // 26`
            		`generating a double-loop to create a header`
            		`header = []`
            		`for i in range(1, n+1)`
                		`for j in s`
                 			 `header += s[j]*i`
            		`data.columns = header #will assign header without changing the dimentions`
 
5) Compute summary statistics:
	- Mean: `np.mean(data)`
	- Standart deviation: `np.std(data)`
	- Median: `np.median(data)`
	
6) Visualize data
	- Show a hystogramme for one feature at a time and write each image into a file:
	    `for i in range(len(data[0]))` 
             	`pyplot.plot(data[:,i]))`
	- Compare 2 features at a time write each image into a file:
          	`j = 0`
          	`for i in range(len(data[0]))` 
              		`for j in range((i+j),len(data[0]))` 
                		`pyplot.skatter(data[:,i], data[:,j]))`
				
----------------

1.	Download the data to local directory
2.	Set up dynamic file input using:
parser.add_argument("file_name") # positional argument parser.add_argument("-header_name", "--header_name", default="default.txt") # optional header file name
file_name = args.file_name if args.header_name:
header_name = args.header_name
3.	Load the data into the DataFrame:
data = pd.read_csv(file_name, sep='\s+|,', header=None)
4.	Add header dynamically
•	if file_name == 'wdbc.data':
o	header = my custom string #for my chosen dataset
o	data.columns = header #will assign header without changing the dimentions
•	for all other datasets:
o	if header_name is a file:
	read one line from header_name, change it to be able to assign it to a list variable
	header = "clean" string of names from file
	obligatory assert to check len(header) == len(data[0])
	data.columns = header #will assign header without changing the dimentions
o	else(if we didn't assign a header file):
	assign column names automatically:
s = sring.ascii_uppercase #create a 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 26 characters
	calculate a var n for the loop to be able to generate a list with non-repetitive chars like AA or AAA to name all the columns:
if col_number % 26 != 0:n = col_number // 26 + 1
	else: n = col_number // 26
	generating a double-loop to create a header
header = []
for i in range(1, n+1)
for j in s
header += s[j]*i
data.columns = header #will assign header without changing the dimentions

5.	Compute summary statistics
•	Mean: 
np.mean(data)
•	Standard deviation:
np.std(data)
•	Median: 
np.median(data)
6.	Visualize data
•	Show a histogram for one feature at a time and write each image into a file:
for i in range(len(data[0]))
pyplot.plot(data[:,i]))
•	Compare 2 features at a time write each image into a file:
j = 0
for i in range(len(data[0]))
for j in range((i+j),len(data[0]))
pyplot.skatter(data[:,i], data[:,j]))



                
          
