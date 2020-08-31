#支持向量回归机预测（径向基函数）
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm

dataset = pd.read_csv('data_wp.csv')
data_input = dataset.iloc[:,:-1].values/1000     
data_output = dataset.loc[:,['pt']].values/1000   
trainlen = int(len(data_input)*0.8)    
testlen = int(len(data_input)-trainlen)   

X_train = data_input[:trainlen].reshape(trainlen,-1)  
y_train = data_output[:trainlen].reshape(trainlen,1)   
X_test = data_input[trainlen:].reshape(testlen,-1)   
y_test = data_output[trainlen:].reshape(testlen,1)   

model_svm = svm.SVR(kernel='rbf')
model_svm.fit(X_train,y_train)
pred = model_svm.predict(X_test)

plt.figure(figsize=(12,18))
plt.subplot(211)
plt.plot(y_test,color='r')
plt.plot(pred,color='k')
plt.xlabel('Number')
plt.ylabel('kWh')
plt.legend(['true value','predict value'])
plt.subplot(212)
plt.plot(y_test[150:300],color='r')
plt.plot(pred[150:300],color='k')
plt.xlabel('Number')
plt.ylabel('kWh')
plt.legend(['true value','predict value'])
plt.tight_layout()
plt.show()