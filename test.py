from random import randint
import DataLoad as dl

from sklearn.linear_model import LogisticRegression

import pickle


def visualTest(itemIndex):
    # it shows the image with it's real numerical value and the predicted numerical value
    predicted = logisticRegr.predict(testdata[itemIndex].reshape(1, -1))
    dl.displayDataImage(test, itemIndex, str(predicted))


# load the saved model during training
filename = 'model/logi-reg-100.sav'
logisticRegr = pickle.load(open(filename, 'rb'))

# load the test dataset
test = dl.loadMnistTest()
testdata = [item[1:] for item in test]
testlabel = [item[0] for item in test]

# visual prediction test
visualTest(randint(0, 10000))


# prints the accuracy of the model
score = logisticRegr.score(testdata, testlabel)
print(str(score*100)+"%")
