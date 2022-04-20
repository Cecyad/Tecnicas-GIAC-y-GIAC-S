import numpy as np 
import pandas as pd
import random

col=4

df8=pd.read_csv('salidac1.csv',header=None)
df9=pd.read_csv('salidac2.csv',header=None)
df10=pd.read_csv('salidac3.csv',header=None)
df11=pd.read_csv('salidac4.csv',header=None)
df12=pd.read_csv('salidac5.csv',header=None)

df13=pd.read_csv('salidacs1.csv',header=None)
df14=pd.read_csv('salidacs2.csv',header=None)
df15=pd.read_csv('salidacs3.csv',header=None)
df16=pd.read_csv('salidacs4.csv',header=None)
df17=pd.read_csv('salidacs5.csv',header=None)

df18=pd.read_csv('SN1.csv',header=None)
df19=pd.read_csv('SN2.csv',header=None)
df20=pd.read_csv('SN3.csv',header=None)
df21=pd.read_csv('SN4.csv',header=None)
df22=pd.read_csv('SN5.csv',header=None)

df23=pd.read_csv('SE1.csv',header=None)
df24=pd.read_csv('SE2.csv',header=None)
df25=pd.read_csv('SE3.csv',header=None)
df26=pd.read_csv('SE4.csv',header=None)
df27=pd.read_csv('SE5.csv',header=None)

df28=pd.read_csv('STL1.csv',header=None)
df29=pd.read_csv('STL2.csv',header=None)
df30=pd.read_csv('STL3.csv',header=None)
df31=pd.read_csv('STL4.csv',header=None)
df32=pd.read_csv('STL5.csv',header=None)

df33=pd.read_csv('SU1.csv',header=None)
df34=pd.read_csv('SU2.csv',header=None)
df35=pd.read_csv('SU3.csv',header=None)
df36=pd.read_csv('SU4.csv',header=None)
df37=pd.read_csv('SU5.csv',header=None)

df38=pd.read_csv('SSE1.csv',header=None)
df39=pd.read_csv('SSE2.csv',header=None)
df40=pd.read_csv('SSE3.csv',header=None)
df41=pd.read_csv('SSE4.csv',header=None)
df42=pd.read_csv('SSE5.csv',header=None)

df43=pd.read_csv('SS1.csv',header=None)
df44=pd.read_csv('SS2.csv',header=None)
df45=pd.read_csv('SS3.csv',header=None)
df46=pd.read_csv('SS4.csv',header=None)
df47=pd.read_csv('SS5.csv',header=None)

df48=pd.read_csv('ST1.csv',header=None)
df49=pd.read_csv('ST2.csv',header=None)
df50=pd.read_csv('ST3.csv',header=None)
df51=pd.read_csv('ST4.csv',header=None)
df52=pd.read_csv('ST5.csv',header=None)

df53=pd.read_csv('ssob1.csv',header=None)
df54=pd.read_csv('ssob2.csv',header=None)
df55=pd.read_csv('ssob3.csv',header=None)
df56=pd.read_csv('ssob4.csv',header=None)
df57=pd.read_csv('ssob5.csv',header=None)

df58=pd.read_csv('salidesvalance.csv',header=None)

c=[]
i=0
l,s=df58.shape
while i < s:
    c.append(round(df58[i].mean(),2))
    i+=1

print("Caso base &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")


c=[]
i=0
l,s=df8.shape
while i < s:
    uno=round(df8[i].mean(),4)
    dos=round(df9[i].mean(),4)
    tres=round(df10[i].mean(),4)
    cuarto=round(df11[i].mean(),4)
    quinto=round(df12[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("GIAC &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")

#print("GIAC")
#print(c)
#print()


c=[]
i=0
l,s=df13.shape
while i < s:
    uno=round(df13[i].mean(),4)
    dos=round(df14[i].mean(),4)
    tres=round(df15[i].mean(),4)
    cuarto=round(df16[i].mean(),4)
    quinto=round(df17[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("GIAC-S &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")

#print("GIAC-A")
#print(c)
#print()

c=[]
i=0
l,s=df53.shape
while i < s:
    uno=round(df53[i].mean(),4)
    dos=round(df54[i].mean(),4)
    tres=round(df55[i].mean(),4)
    cuarto=round(df56[i].mean(),4)
    quinto=round(df57[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("Sobremuestreo &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6]," \\\ \hline")

c=[]
i=0
l,s=df33.shape
while i < s:
    uno=round(df33[i].mean(),4)
    dos=round(df34[i].mean(),4)
    tres=round(df35[i].mean(),4)
    cuarto=round(df36[i].mean(),4)
    quinto=round(df37[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("Submuestreo &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")


c=[]
i=0
l,s=df43.shape
while i < s:
    uno=round(df43[i].mean(),4)
    dos=round(df44[i].mean(),4)
    tres=round(df45[i].mean(),4)
    cuarto=round(df46[i].mean(),4)
    quinto=round(df47[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("SMOTE &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")

c=[]
i=0
l,s=df28.shape
while i < s:
    uno=round(df28[i].mean(),4)
    dos=round(df29[i].mean(),4)
    tres=round(df30[i].mean(),4)
    cuarto=round(df31[i].mean(),4)
    quinto=round(df32[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("SMOTETomeK Links &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")
#print("Tomelinks")
#print(c)
#print()

c=[]
i=0
l,s=df38.shape
while i < s:
    uno=round(df38[i].mean(),4)
    dos=round(df39[i].mean(),4)
    tres=round(df40[i].mean(),4)
    cuarto=round(df41[i].mean(),4)
    quinto=round(df42[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("SMOTEENN &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")
#print("smoteENN")
#print(c)
#print()


c=[]
i=0
l,s=df18.shape
while i < s:
    uno=round(df18[i].mean(),4)
    dos=round(df19[i].mean(),4)
    tres=round(df20[i].mean(),4)
    cuarto=round(df21[i].mean(),4)
    quinto=round(df22[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("Nearmiss &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")
#print("Nearmiss")
#print(c)
#print()

c=[]
i=0
l,s=df23.shape
while i < s:
    uno=round(df23[i].mean(),4)
    dos=round(df24[i].mean(),4)
    tres=round(df25[i].mean(),4)
    cuarto=round(df26[i].mean(),4)
    quinto=round(df27[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("ENN &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")

c=[]
i=0
l,s=df48.shape
while i < s:
    uno=round(df48[i].mean(),4)
    dos=round(df49[i].mean(),4)
    tres=round(df50[i].mean(),4)
    cuarto=round(df51[i].mean(),4)
    quinto=round(df52[i].mean(),4)
    sexto=(uno+dos+tres+cuarto+quinto)/5
    c.append(round(sexto,2))
    i+=1

print("SMOTETomek &",c[0],",",c[1],"&",c[2],",",c[3],"&",c[4],",",c[5],",",c[6],"\\\ \hline")

