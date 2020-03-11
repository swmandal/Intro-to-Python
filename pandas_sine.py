#Pandas_SINE.PY
#SWARUP
#Mar/10/2020
# https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/



#1.  import modules
#2.  file read
#3.  Determine what families are in there (SINE, etc)
#4.  Create new dataframe from that file using only elements in family “SINE” 
#5.  Drop columns “Strand” and “Score”
#6.  Create new column “Length”
#7.  Determine min, max, and mean for all SINEs
#8.  Determine min, max, and mean length for each sub-family of SINE (metulj and ZenoSINE)


# import modules
import pandas as pd

#read in m csv file using the 'forward-slash t' command since bed files use a tab to seperate columns.
print("Read in bed file ...")
avan = pd.read_csv('aVan_rm.bed', sep='\t', header=None)
header = ['Scaffold', 'Start', 'Stop', 'Element', 'Score', 'Strand', 'Family', 'Sub-family', 'Divergence' ]
avan.columns = header[:len(avan.columns)]
print(avan.head())

#3. number of families are there, each family would be unique 
print("Unique family names = ", avan.Family.unique())
print("There are 5 unique families")

#4. Create new dataframe from that file using only elements in family “SINE” 
SINE = avan[avan["Family"]=="SINE"]
print (SINE)

#5.drop the colums strand and score
print("Dropping columns 'Strand' and 'Score' :")
SINE_DROP = avan.drop(["Score", "Strand"], axis=1)
print(SINE_DROP.head())

#6. Create new column “Length”
#SINE_DROP["Length"] = (SINE_DROP['Stop'] - SINE_DROP[Strat']
print("Now creating a new column name 'Length', which is the difference between 'Stop' and 'Start'",)
print(SINE_DROP.head())
  
#7.Determine min, max, and mean for all SINEs
min_sine = SINE_DROP['Length'].min()
max_sine = SINE_DROP['Length'].max()
mean_sine = SINE_DROP['Length'].mean()
print("The Minimum, Maximum and Mean of SINE is:", min_sine,";", max_sine,";", mean_sine)
