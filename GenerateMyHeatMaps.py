import pandas as pd
import os
import gmplot

print(os.getcwd())
#load data
df1 = pd.read_csv(r"C:\Users\samou\Desktop\Python\HeatMap Project\track_points.csv", header=None)
df2 = pd.read_csv(r"C:\Users\samou\Desktop\Python\HeatMap Project\Run2.csv", header=None)
dfcomp = pd.read_csv(r"C:\Users\samou\Desktop\Python\HeatMap Project\CompiledRuns.csv", header=None)

#Step 1: clean data:
#Get rid of extraneous columns that aren't related to latitude, longitude
df1.drop([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],axis=1,inplace=True)
df1.drop([0],axis=0,inplace=True)
df2.drop([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],axis=1,inplace=True)
df2.drop([0],axis=0,inplace=True)
dfcomp.drop(0,axis=0,inplace=True)

#rename x, y to long,lat
df1.rename(columns={0:'Longitude', 1:'Latitude'}, inplace=True)
df2.rename(columns={0:'Longitude', 1:'Latitude'}, inplace=True)
dfcomp.rename(columns={0:'Longitude',1:'Latitude'}, inplace=True)

#Step 2: combine latitude and longitude using pd.concat()
df3 = pd.concat([df1,df2,dfcomp])

#Not sure this is necessary
#Yes this is necessary, the gmplots package will throw a d_type related error if data type isn't changed
#because the data is a python object type and not an int/float
Latitude = df3['Latitude']
Latitude = Latitude.astype(str).astype(float)
Longitude = df3['Longitude']
Longitude = Longitude.astype(str).astype(float)

#Step 3: overlay latitude and longitude on maps using code from other file (done)
#generate gmaps basemap for overlaying run data (lat, long set to Sydney), API key
mymap = gmplot.GoogleMapPlotter(33.86,151.20,13,'MY API KEY HERE')

#pass lat, long from dataframe to gmplot heatmap function
mymap.heatmap(Latitude, Longitude)
mymap.draw("letsgo.html")

#now what? this is clunky and requires direct changes to the code for every run added
#think about automating the data cleaning to be cleaner as per OOP practices
