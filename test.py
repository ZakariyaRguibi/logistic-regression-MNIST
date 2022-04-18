import DataLoad as dl

from sklearn.linear_model import LogisticRegression

import pickle

data = dl.loadMnistTraining()

filename = 'model/logi-reg-10000.sav'
logisticRegr = pickle.load(open(filename, 'rb'))


test = dl.loadMnistTest()
testdata = [item[1:] for item in test]
testlabel = [item[0] for item in test]

print(logisticRegr.predict(testdata[1].reshape(1, -1)))
dl.displayDataImage(test, 1)

score = logisticRegr.score(testdata, testlabel)

print(str(score*100)+"%")
