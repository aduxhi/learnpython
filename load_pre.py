
#最小二乘法-------线性回归
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

dataset = pd.read_csv('data_wp.csv')
data_input = dataset.iloc[:,:-1].values  
data_output = dataset.loc[:,['pt']].values  
trainlen = int(len(data_input)*0.8)    
testlen = int(len(data_input)-trainlen)     

X_train = data_input[:trainlen].reshape(trainlen,-1)  
y_train = data_output[:trainlen].reshape(trainlen,1)    
X_test = data_input[trainlen:].reshape(testlen,-1)   
y_test = data_output[trainlen:].reshape(testlen,1)   

model_line = linear_model.LinearRegression()   
model_line.fit(X_train,y_train)
pred = model_line.predict(X_test)

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