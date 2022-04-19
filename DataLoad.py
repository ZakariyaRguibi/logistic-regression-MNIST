from numpy import genfromtxt
import matplotlib.pyplot as plt
import csv


def loadCsvData(filePath, headerSkips=1, type=int):
    """load a csv file 

     Parameters:
        filePath (str): The path of the csv file
        headerSkips (int):The number of lines to skip at the beginning of the file.
        type (class): DataType of the csv values {int,float, String}
     Returns:
        array
    """
    return genfromtxt(filePath,
                      delimiter=',', skip_header=headerSkips, dtype=type)


def displayDataImage(data, index, predicted=""):
    """Display a DataImage """
    img = data[index][1:].reshape((28, 28))
    plt.imshow(img, cmap="Greys",)

    extraText = "Predicted : " + predicted if predicted else ""

    plt.title("label " + str(data[index][0])+" " + extraText)
    plt.show()


def loadMnistTraining():
    return loadCsvData("dataset/mnist_train.csv")


def loadMnistTest():
    return loadCsvData("dataset/mnist_test.csv")


# data = loadMnistTest()
# displayDataImage(data, 1)
