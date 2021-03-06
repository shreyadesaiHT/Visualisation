import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt 
from datetime import datetime
from numerize import numerize

path = pd.read_csv(r"C:/Users/ws_htu768/Desktop/Scripts/Portwise/north.csv")
#path =r"D:\skv_ML_data\port_wise\All_data\iq.csv"
#port_num =int(input("Enter the port number:: "))
#port_num =int(sys.argv[1])
#month=int(sys.argv[2])
arguments=len(sys.argv)-1
if arguments==0:
    port_num=2775
    month=3
elif arguments==1:
    port_num=int(sys.argv[1])
    month=3
elif arguments==2:
    port_num=int(sys.argv[1])
    month=int(sys.argv[2])

data = path
df= pd.DataFrame(data)
df.sort_values(by=["SUBMIT_DATE"])

df1=df.copy()
df1['month'] = pd.DatetimeIndex(df1['SUBMIT_DATE']).month

s1=[]
for j in df1.PORT_NO:
        s1.append(j)

s2=[]    
for j in s1:
    if j not in s2:
        s2.append(j) 

d_new1 = df1.loc[(df1["PORT_NO"]==port_num) & (df1["month"]==month) ]
d_new1.sort_values(by=["SUBMIT_DATE"],inplace=True)

s3=[]
if port_num in s2:
	s3.append(port_num)


for i in range(1):

    
    if port_num in s3:
        print("Valid Port number")

        name= s3[i]
        s_name =str(name)
        y1=d_new1['TOTAL_SUBMIT_CHR_COUNT']
        x1=d_new1['SUBMIT_DATE']
        #print(df1.columns)
        #print(y1)
        #dpi=100
        fd=plt.figure(figsize=(16,9), dpi=100)
        #fd.set_figwidth(10)
        #fd.set_figheight(15)
        #plt.set_figwidth()
        #plt.set_figheight(4)
        plt.xticks(rotation=90)
        plt.plot(x1,y1,'ro-')
        plt.grid()
        plt.gca().set(title="Trend for Port :: "+ s_name , xlabel="DATE", ylabel="Count in millions")
        for x,y in zip(x1,y1):
            #label = "{:d}".format(y)
            label =numerize.numerize(y)
            plt.annotate(label, # this is the text
            (x,y), # these are the coordinates to position the label
            textcoords="offset points", # how to position the text
            xytext=(0,10), # distance from text to points (x,y)
            ha='center',rotation=90)
        
        plt.savefig("C:/Users/ws_htu768/Desktop/Scripts/Portwise/IMG/"+ "Port_"+s_name + ".png")
        #plt.show()
   