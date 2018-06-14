__author__ = "Praahas Amin"
__credits__ = ["Tom M.Mitchell"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Praahas Amin"
__email__ = "praahas@gmail.com"
__status__ = "Production"

#FIND-S ALGORITHM
#This algorithm is the first program in the Machine Learning Laboratory Course 15CSL76 under VTU.
#The theory behind the algorithm is based on the description given by Tom M. Mitchell in Machine Learning

import pandas as pd 				#Pandas must be installed.Pandas used for reading data from .csv file. 
data = pd.read_csv('enjoysport.csv')
columnLength= data.shape[1]			#obtain number of columns
rowLength=data.shape[0]				#obtain number of rows
print (data)						#print the table
h=['0','0','0','0','0','0']			#initialize  h to the most specific hypothesis in the Hypotheses Space H
hp=[]								#initialize list hp i.e list of hypotheses for positive training examples
hn=[]								#initialize list hn i.e list of hypotheses for all negative training examples
for i in range(rowLength):			#this loop is used to build the hypothesis list for every row.
	trainingExample=[]							#initialize list trainingExample used to hold a hypothesis after fetching it from .csv file
	trainingExample.append(data.sky[i])			# every column value for a row is fetched and appended to trainingExample
	trainingExample.append(data.airTemp[i])
	trainingExample.append(data.humidity[i])
	trainingExample.append(data.wind[i])
	trainingExample.append(data.water[i])
	trainingExample.append(data.forecast[i])
	if data.enjoySport[i]!='no':	#if the trainingExample is positive, then it is appended to hp else to hn
		hp.append(trainingExample)
	else:
		hn.append(trainingExample)
for i in range (len(hp)):			#update the hypothesis h from most specific to maximally specific
	for j in range(columnLength-1):	#if the hypothesis attribute value is 0, it is updated to the attributes in the first hypothesis
		if (h[j]=='0'):				
			h[j]=hp[i][j]			
		if (h[j]!=hp[i][j]):		#if the attribute value in the hypothesis is not same as the attribute value in the successive hypotheses
			h[j]='?'				#then it is updated to '?' indicating that any value is acceptable.
		else:						#if the attribute in the hypothesis is the same as the attribute value in the successive hypotheses
			h[j]=hp[i][j]			#then the same attribute value is retained
print('\n')
print('The positive Hypotheses are')			
print(hp)

print('\n')
print('The negative Hypotheses are')			
print(hn)
			
print('\n')
print('The Maximally Specific Hypothesis h is')			
print(h)