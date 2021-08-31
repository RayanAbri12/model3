#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:05:25 2019

@author: rayan
"""

import pandas as pd
#import numpy as np
import os
import glob
from matplotlib import pyplot as plt

def Ocak(i):
    switcher={
             1:'-01-01',
             2:'-01-02',
             3:'-01-03',
             4:'-01-04',
             5:'-01-05',
             6:'-01-06',
             7:'-01-07',
             8:'-01-08',
             9:'-01-09',
             10:'-01-10',
             11:'-01-11',
             12:'-01-12',
             13:'-01-13',
             14:'-01-14',
             15:'-01-15',
             16:'-01-16',
             17:'-01-17',
             18:'-01-18',
             19:'-01-19',
             20:'-01-20',
             21:'-01-21',
             22:'-01-22',
             23:'-01-23',
             24:'-01-24',
             25:'-01-25',
             26:'-01-26',
             27:'-01-27',
             28:'-01-28',
             29:'-01-29',
             30:'-01-30',
             31:'-01-31'
             }
    return switcher.get(i,"Invalid day of month")

          
def Process(ss):
    f = open(ss)
    ff= open("tempFile.txt","w+")
    line = f.readline()
    
    while line:
         
        print(line)
        # use realine() to read next line
        line = f.readline()
        if "#" not in line:
            ff.write(line)
    
    f.close() 
    ff.close()    
    df = pd.read_csv("tempFile.txt", names=['Tarih ve Saat', 'TEC'], delimiter=' ')
    os.remove("tempFile.txt")
    print("File Removed!")
    
    df['Tarih ve Saat'] =  pd.to_datetime(df['Tarih ve Saat'])
    
    df['Tarih ve Saat']= df['Tarih ve Saat'].astype('str')
    print(df['Tarih ve Saat'])
    df[['Tarih','Saat']] = df['Tarih ve Saat'].str.split(" ",expand=True)
    df['Tarih']= df['Tarih'].astype('str')
    df['Saat']= df['Saat'].astype('str')
    strg = df['Tarih'].iloc[0]
    if(Ocak(1) in strg):
        df['Sample'] = df['Saat'].str.contains(':00:00|:30:00|:45:00|:15:00', regex=True)
    if(Ocak(2) in strg): 
        df['Sample'] = df['Saat'].str.contains(':01:00|:31:00|:46:00|:16:00', regex=True)
    if(Ocak(3) in strg): 
        df['Sample'] = df['Saat'].str.contains(':02:00|:32:00|:47:00|:17:00', regex=True)
    if(Ocak(4) in strg): 
        df['Sample'] = df['Saat'].str.contains(':03:00|:33:00|:48:00|:18:00', regex=True)
    if(Ocak(5) in strg): 
        df['Sample'] = df['Saat'].str.contains(':04:00|:34:00|:49:00|:19:00', regex=True)
    if(Ocak(6) in strg): 
        df['Sample'] = df['Saat'].str.contains(':05:00|:35:00|:50:00|:20:00', regex=True)
    if(Ocak(7) in strg): 
        df['Sample'] = df['Saat'].str.contains(':06:00|:36:00|:51:00|:21:00', regex=True)
    if(Ocak(8) in strg): 
        df['Sample'] = df['Saat'].str.contains(':07:00|:37:00|:52:00|:22:00', regex=True)
    if(Ocak(9) in strg): 
        df['Sample'] = df['Saat'].str.contains(':08:00|:38:00|:53:00|:23:00', regex=True)
    if(Ocak(10) in strg): 
        df['Sample'] = df['Saat'].str.contains(':09:00|:39:00|:54:00|:24:00', regex=True)
    if(Ocak(11) in strg): 
        df['Sample'] = df['Saat'].str.contains(':10:00|:40:00|:55:00|:25:00', regex=True)
    if(Ocak(12) in strg): 
        df['Sample'] = df['Saat'].str.contains(':11:00|:41:00|:56:00|:26:00', regex=True)
    if(Ocak(13) in strg): 
        df['Sample'] = df['Saat'].str.contains(':12:00|:42:00|:57:00|:27:00', regex=True)
    if(Ocak(14) in strg): 
        df['Sample'] = df['Saat'].str.contains(':13:00|:43:00|:58:00|:28:00', regex=True)
    if(Ocak(15) in strg): 
        df['Sample'] = df['Saat'].str.contains(':14:00|:44:00|:59:00|:29:00', regex=True)
    if(Ocak(16) in strg): 
        df['Sample'] = df['Saat'].str.contains(':15:00|:45:00|:00:00|:30:00', regex=True)
    if(Ocak(17) in strg): 
        df['Sample'] = df['Saat'].str.contains(':16:00|:46:00|:01:00|:31:00', regex=True)
    if(Ocak(18) in strg): 
        df['Sample'] = df['Saat'].str.contains(':17:00|:47:00|:02:00|:32:00', regex=True)
    if(Ocak(19) in strg): 
        df['Sample'] = df['Saat'].str.contains(':18:00|:48:00|:03:00|:33:00', regex=True)
    if(Ocak(20) in strg): 
        df['Sample'] = df['Saat'].str.contains(':19:00|:49:00|:04:00|:34:00', regex=True)
    if(Ocak(21) in strg): 
        df['Sample'] = df['Saat'].str.contains(':20:00|:50:00|:05:00|:35:00', regex=True)
    if(Ocak(22) in strg): 
        df['Sample'] = df['Saat'].str.contains(':21:00|:51:00|:06:00|:36:00', regex=True)
    if(Ocak(23) in strg): 
        df['Sample'] = df['Saat'].str.contains(':22:00|:52:00|:07:00|:37:00', regex=True)    
    if(Ocak(24) in strg): 
        df['Sample'] = df['Saat'].str.contains(':23:00|:53:00|:08:00|:38:00', regex=True)
    if(Ocak(25) in strg): 
        df['Sample'] = df['Saat'].str.contains(':24:00|:54:00|:09:00|:39:00', regex=True)
    if(Ocak(26) in strg): 
        df['Sample'] = df['Saat'].str.contains(':25:00|:55:00|:10:00|:40:00', regex=True)
    if(Ocak(27) in strg): 
        df['Sample'] = df['Saat'].str.contains(':26:00|:56:00|:11:00|:41:00', regex=True)
    if(Ocak(28) in strg): 
        df['Sample'] = df['Saat'].str.contains(':27:00|:57:00|:12:00|:42:00', regex=True)
    if(Ocak(29) in strg): 
        df['Sample'] = df['Saat'].str.contains(':28:00|:58:00|:13:00|:43:00', regex=True)
    if(Ocak(30) in strg): 
        df['Sample'] = df['Saat'].str.contains(':29:00|:59:00|:14:00|:44:00', regex=True)
    if(Ocak(31) in strg): 
        df['Sample'] = df['Saat'].str.contains(':30:00|:00:00|:15:00|:45:00', regex=True)    
    df['Sample']= df['Sample'].astype('str')
    df = df.drop(df.index[df['Sample'].str.contains('False',  regex=True)])
    del df['Tarih ve Saat']
    del df['Sample']
    df1 = df
    for index, row in df1.iterrows():
        a = row['Saat']
        df1[a]= row['TEC']
    
    del df1['TEC'], df1['Saat']
    df1=df1.drop(df.index[1:])
#    df1.columns = [''] * len(df1.columns)
    return df1    
 
#df = Process('/home/rayan/Downloads/my_phd/ksmv/ksmv-2014/1/ksmv_20140108.txt')    
txt_files = glob.glob("/home/rayan/Dropbox/ksmv-2013/*.txt")

listf = []
dff = pd.DataFrame()

dff1 = pd.DataFrame()

for x in range(1,len(txt_files)):
   listf.append(Process(txt_files[x]))
  
   q = Process(txt_files[x])
   q.columns = [''] * len(q.columns)
   dff = dff.append(q)
   
#dff = pd.DataFrame(columnsnames=list(range(1,97)))
dff.columns = list(range(0,97))

#df4 = pd.DataFrame(listf, columns = ['z'])

#for row in listf:
#    for row1 in row:
#        if (type(row1) != 'str'):
#            dff1 = dff1.append(row1)

#last = pd.DataFrame()
#
#
#for index, row in dff.iterrows():
#    for element in row:
#        row = row[~row.isnull()]
#    
#    last = last.append(row)
        


dff.to_csv('2013.csv',index=False)




#fg = Process(st.replace("*","1"))
    
    
    

