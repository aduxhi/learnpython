#深度神经网络预测
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from keras.models import Sequential
from keras import regularizers
from keras.layers import Dense
from sklearn import preprocessing

dataset = pd.read_csv('data_wp.csv')
min_max_scaler_input = preprocessing.MinMaxScaler()     
min_max_scaler_output = preprocessing.MinMaxScaler()    


data_output = dataset.loc[:,['pt']].values  
data_input = dataset.iloc[:,:-1].values   
trainlen = int(len(data_input)*0.8)  
testlen = int(len(data_input)-trainlen)     

train_output = data_output[:trainlen] 
test_output = data_output[trainlen:]    

data_input = min_max_scaler_input.fit_transform(data_input)     
data_output = min_max_scaler_output.fit_transform(data_output)      

x_train = data_input[:trainlen].reshape(trainlen,-1)   
x_test = data_output[:trainlen].reshape(trainlen,1)   
y_train = data_input[trainlen:].reshape(testlen,-1)   
y_test = data_output[trainlen:].reshape(testlen,1)    

model = Sequential()
model.add(Dense(64, input_dim=data_input.shape[1], activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(1, activation='linear', kernel_regularizer=regularizers.l1(0.01)))
model.compile(loss='mse',optimizer='adam')
loss = model.fit(x_train, x_test,epochs=20,verbose=2,batch_size=50)

test_dnn = model.predict(y_train)
test_dnn = min_max_scaler_output.inverse_transform(test_dnn.reshape(-1,1))/1000
test_output = min_max_scaler_output.inverse_transform(y_test.reshape(-1,1))/1000

plt.figure(figsize=(12,18))
plt.subplot(211)
plt.plot(test_output,color='r')
plt.plot(test_dnn,color='k')
plt.xlabel('Number')
plt.ylabel('Wh')
plt.legend(['true value','predict value'],loc='upper right')
plt.subplot(212)
plt.plot(test_output[150:300],color='r')
plt.plot(test_dnn[150:300],color='k')
plt.xlabel('Number')
plt.ylabel('Wh')
plt.legend(['true value','predict value'],loc='upper right')
plt.tight_layout()
plt.show()