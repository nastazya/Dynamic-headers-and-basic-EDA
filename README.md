# class5_homework


1.  Download the data to local directory.
2.  Set up dynamic file input using `argparse`.
3.  Load the data into the DataFrame (`data = pd.read_csv(myfile, sep='\s+|,', header=None)`)
4.  Add header dynamicly.
5.  Compute summary statistics:
    5.1.  Mean: `np.mean(data)` 
    5.2.  Standart deviation: `np.std(data)`
    5.3.  Median: `np.median(data)`
6.  Visualize data
    6.1.  Feature at a time:
          `for i in range(len(data[0])) 
             `pyplot.plot(data[:,i]))
    6.2.  Compare 2 features at a time
          `j = 0
          `for i in range(len(data[0])) 
              `for j in range((i+j),len(data[0])) 
                `pyplot.skatter(data[:,i], data[:,j]))
                
          
