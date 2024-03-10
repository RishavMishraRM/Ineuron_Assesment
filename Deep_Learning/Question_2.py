# -*- coding: utf-8 -*-
"""mnist_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JRT10ZQy-e6BY-q21ThmXTdC8DBNJDEo
"""

import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten

(X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()

X_test.shape

y_train

import matplotlib.pyplot as plt
plt.imshow(X_train[2])

X_train = X_train/255
X_test = X_test/255

X_train[0]

model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),
    Dense(10, activation='softmax')
])

model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train,y_train,epochs=10,validation_split=0.2)

y_prob = model.predict(X_test)

y_pred = y_prob.argmax(axis=1)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.imshow(X_test[1])

model.predict(X_test[1].reshape(1,28,28)).argmax(axis=1)

