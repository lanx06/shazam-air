from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from classifier import prepareData

# prepare the data and analysis the pca and lca

data = pd.read_csv("./dataset/elecfeatures/beatsdataset.csv")
data = data.loc[:, '1-ZCRm':'class']

dataColRanges = ('1-ZCRm', '34-ChromaDeviationm')
labelCol = 'class'
data_set = prepareData.Classifer_dataset("../data/data_set/beatsdataset.csv")
label, data = data_set.prepareData(dataColRanges, labelCol, True)

fig1 = data_set.plotPCA()
fig2 = data_set.plotLDA()

# train a model here and save it in .h5 file
print("Construct the model")

Dnn = Sequential()
Dnn.add(Dense(50, activation='relu', input_dim = 34))
Dnn.add(Dense(50, activation='relu'))
Dnn.add(Dense(100, activation='relu'))
Dnn.add(Dense(50, activation='relu'))
# Dnn_3.add(Dense(100, activation='relu'))
# Dnn_3.add(Dense(100, activation='relu'))
# Dnn_3.add(Dense(50, activation='relu'))
Dnn.add(Dense(50, activation='relu'))
Dnn.add(Dense(23, activation = 'softmax'))

Dnn.compile(metrics=['accuracy'], optimizer='Adam', loss='mean_squared_error')

print("Start training")
Dnn.fit(data, label, validation_split = 0.0, epochs = 100, batch_size=100, shuffle = True)

Dnn.save("./demo.h5")