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
import sys
from imblearn.under_sampling import EditedNearestNeighbours 

valor=8

a = int(sys.argv[1])
aa= int(sys.argv[2])

if aa==1:
    df2=pd.read_csv('test1.csv',header=None)
if aa==2:
    df2=pd.read_csv('test2.csv',header=None)
if aa==3:
    df2=pd.read_csv('test3.csv',header=None)
if aa==4:
    df2=pd.read_csv('test4.csv',header=None)
if aa==5:
    df2=pd.read_csv('test5.csv',header=None)


df=pd.read_csv('completo.csv',header=None)
#df2=pd.read_csv('test.csv',header=None)

minoritaria=df2[df2.iloc[:, -1]==1]

#tecnicas-----------------

if a==1:
    os=SMOTETomek()
if a==2:
    os = SMOTE()
if a==3:
    os = SMOTEENN()
if a==4:
    os = RandomUnderSampler()
if a==5:
    os = TomekLinks()
if a==6:
    os = NearMiss()
if a==7:
    os=EditedNearestNeighbours()





x=np.array(df)

X_train, y_train = os.fit_sample(np.array(x[:,:valor]), np.array(x[:,valor]))






tx=pd.DataFrame(X_train)
ty=pd.DataFrame(y_train)

ty=ty.rename(columns={0:valor})
artificial=pd.concat([tx,ty], axis=1)


completo=pd.concat([df2,artificial], axis=0)
completo.reset_index(drop=True, inplace=True)


#eliminar instancias repetidas
dff=completo.drop_duplicates( keep=False)
dff.reset_index(drop=True, inplace=True)



x2=np.array(dff)

X_tt, y_tt = os.fit_sample(np.array(x2[:,:valor]), np.array(x2[:,valor]))

y_t=pd.DataFrame(y_tt)


test_d=np.array(df2.iloc[:,:valor])
test_c=np.array(df2.iloc[:,-1])


sc=StandardScaler()
X_train=sc.fit_transform(X_tt)
X_test=sc.transform(test_d)



#print("KNN")
algoritmo = KNeighborsClassifier(n_neighbors = 5,p=1)
algoritmo.fit(X_train,y_tt)
c,e=algoritmo.kneighbors(X_test,n_neighbors = 5, return_distance=True)
y_pred = algoritmo.predict(X_test)


#print("red neuronal")
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=10000)
mlp.fit(X_train,y_tt)
predictions = mlp.predict(X_test)



#print("Árboles de decisión")
tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(X_train,y_tt)
pre=tree.predict(X_test)




#print("Máquinas de soporte vectorial")
modelo = SVC()
modelo.fit(X_train,y_tt)
predicciones = modelo.predict(X_test)

#print("Bosque aleatorio")
bosque=RandomForestClassifier()
bosque.fit(X_train,y_tt)
predecir=bosque.predict(X_test)



voto=[]
voto.append(y_pred)
voto.append(predictions)
voto.append(pre)
voto.append(predecir)
voto.append(predicciones)

voto1 = np.array(voto)

lu=len(voto1[0])
i=0
voto=[]
punto=0
while i < lu:
    punto=voto1[0][i]+voto1[1][i]+voto1[2][i]+voto1[3][i]+voto1[3][i]
    if punto>2:
        voto.append(1)
    else:
        voto.append(0)
    i+=1
    punto=0

resulados=precision_recall_fscore_support(test_c, voto, average=None)

accuracyy=accuracy_score(test_c, voto)
print(resulados[0][0],resulados[0][1],resulados[1][0],resulados[1][1],resulados[2][0],resulados[2][1],accuracyy, sep=",")

