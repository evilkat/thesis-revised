import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation

seq_length = 5
x = [[i+j for j in range(seq_length)] for i in range(100)]
x_simple = [[i for i in range(4,104)]]
x = np.array(x)
x_simple = np.array(x_simple)

y =[[ i+(i-1)*.5+(i-2)*.2+(i-3)*.1 for i in range(4,104)]]
y =np.array(y)
x_simple=x_simple.reshape((100,1))
x=x.reshape((100,5,1))
y=y.reshape((100,1))

model = Sequential()
model.add(LSTM(8,input_shape=(5,1),return_sequences=False))#True = many to many
model.add(Dense(2,kernel_initializer='normal',activation='linear'))
model.add(Dense(1,kernel_initializer='normal',activation='linear'))
model.compile(loss='mse',optimizer ='adam',metrics=['accuracy'])
model.fit(x,y,epochs=2000,batch_size=5,validation_split=0.05,verbose=0);
scores = model.evaluate(x,y,verbose=1,batch_size=5)
print('Accurracy: {}'.format(scores[1])) 
import matplotlib.pyplot as plt
predict=model.predict(x)
plt.plot(y, predict-y, 'C2')
plt.ylim(ymax = 3, ymin = -3)
plt.show()

model2 = Sequential()
model2.add(Dense(8, input_dim=1, activation= 'linear' ))
model2.add(Dense(2, activation= 'linear' ))
model2.add(Dense(1, activation= 'linear' ))
model2.compile(loss='mse',optimizer='rmsprop',metrics=['accuracy'])
model2.fit(x_simple,y,epochs=2000,batch_size=5,validation_split=0.05,verbose=0);
scores2 = model2.evaluate(x_simple,y,verbose=1,batch_size=5)
print('Accurracy: {}'.format(scores2[1]))