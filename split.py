from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import NearMiss
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTETomek
from imblearn.ensemble import BalancedBaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from imblearn.ensemble import EasyEnsembleClassifier
from imblearn.under_sampling import TomekLinks
from imblearn.combine import SMOTEENN
import numpy as np 
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import DistanceMetric
from operator import itemgetter
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.svm import SVC

valor=8


df=pd.read_csv('diabetes.csv',header=None)
df=df.sort_values(valor).drop_duplicates(subset=[0,1,2,3,4,5,6,7], keep='last').sort_index()
df.reset_index(drop=True, inplace=True)


mm=len(df)
mmin=len(df[df.iloc[:, -1]==1])

print(mm)
#print(mmin)

may=df[df.iloc[:, -1]==0]
minn=df[df.iloc[:, -1]==1]

print("may=",len(may), "min= ",len(minn))

pmay=int(len(may)/5)
pmin=int(len(minn)/5)

print("may = ", pmay, "min = ", pmin)

df2=df.sample(frac=1).reset_index(drop=True)

mayy=df2[df2.iloc[:, -1]==0].reset_index(drop=True)

mino=df2[df2.iloc[:, -1]==1].reset_index(drop=True)


pm=pmay
m1=mayy[0:pmay]
pm+=pmay
m2=mayy[pmay:pm]
p=pm
pm+=pmay
m3=mayy[p:pm]
p=pm
pm+=pmay
m4=mayy[p:pm]
p=pm
pm+=pmay
m5=mayy[p:pm]

pm=pmin
m11=mino[0:pmin]
pm+=pmin
m22=mino[pmin:pm]
p=pm
pm+=pmin
m33=mino[p:pm]
p=pm
pm+=pmin
m44=mino[p:pm]
p=pm
pm+=pmin
m55=mino[p:pm]




tes_x1=pd.concat([m1,m11], axis=0).sort_index()
tes_x1=tes_x1.sample(frac=1).reset_index(drop=True)


tes_x2=pd.concat([m2,m22], axis=0).sort_index()
tes_x2=tes_x2.sample(frac=1).reset_index(drop=True)


tes_x3=pd.concat([m3,m33], axis=0).sort_index()
tes_x3=tes_x3.sample(frac=1).reset_index(drop=True)


tes_x4=pd.concat([m4,m44], axis=0).sort_index()
tes_x4=tes_x4.sample(frac=1).reset_index(drop=True)


tes_x5=pd.concat([m5,m55], axis=0).sort_index()
tes_x5=tes_x5.sample(frac=1).reset_index(drop=True)




df.to_csv('completo.csv',index=False, header=False)
tes_x1.to_csv('test1.csv',index=False, header=False)
tes_x2.to_csv('test2.csv',index=False, header=False)
tes_x3.to_csv('test3.csv',index=False, header=False)
tes_x4.to_csv('test4.csv',index=False, header=False)
tes_x5.to_csv('test5.csv',index=False, header=False)






