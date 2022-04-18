import DataLoad as dl

from sklearn.linear_model import LogisticRegression

import pickle

data = dl.loadMnistTraining()

filename = 'trained/logi-reg-10000.sav'
logisticRegr = pickle.load(open(filename, 'rb'))


test = dl.loadMnistTest()
testdata = [item[1:] for item in test]
testlabel = [item[0] for item in test]


score = logisticRegr.score(testdata, testlabel)

print(str(score*100)+"%")
