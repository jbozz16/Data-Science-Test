#####importing libraries
import pandas as pd
import os

######setting directory

############current directory
os.getcwd()

###########setting directory
os.chdir("C:/Users/User/Desktop/Data_Project/data_sets")

#############importing data set
test = pd.read_csv('spread_test.csv', sep=';')
#############printing name of column
print(test.columns)
########### selecting variables
test1 = test.loc[:,['durata','data_inizio_cardine','data_fine_cardine']]
type(test1)
test1.head()
test1.info()

########## creating new variable
test1['conc'] = test1['data_inizio_cardine'] + '-' + test1['data_fine_cardine']

######### selecting variable
test1 = test1.loc[:,['durata','conc']]

######### printing the type variable
#test1.dtypes

test1['durata'] = test1['durata'].str.replace(',','.').astype('float')

#########group by
test2 = test1.groupby(['conc']).sum()

####################finaly done!!!!!!!