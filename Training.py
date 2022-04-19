import DataLoad as dl

from sklearn.linear_model import LogisticRegression

import pickle

# load the training dataset
data = dl.loadMnistTraining()

# split the dataset to labels and image data
labels = [item[0] for item in data]
imageData = [item[1:] for item in data]

# set the maximum training iterations, the default value is 100
maxTrainingIterations = 100

# load the model
logisticRegr = LogisticRegression(max_iter=maxTrainingIterations)

# fit the model
logisticRegr.fit(imageData, labels)

# save the model
filename = 'model/logi-reg-'+str(maxTrainingIterations)+'.sav'
pickle.dump(logisticRegr, open(filename, 'wb'))
