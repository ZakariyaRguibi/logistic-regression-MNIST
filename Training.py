import DataLoad as dl

from sklearn.linear_model import LogisticRegression

import pickle

data = dl.loadMnistTraining()

labels = [item[0] for item in data]
imageData = [item[1:] for item in data]

logisticRegr = LogisticRegression(max_iter=10000)

logisticRegr.fit(imageData, labels)

test = dl.loadMnistTest()
testdata = [item[1:] for item in test]
testlabel = [item[0] for item in test]


filename = 'model/logi-reg-10000.sav'
pickle.dump(logisticRegr, open(filename, 'wb'))
