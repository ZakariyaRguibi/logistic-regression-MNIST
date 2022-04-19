# Using Logistic regression On MNIST Dataset using python

This project is a python example of logistic regression model training using python,
it contains 3 main files:

- **DataLoad.py** : A helper file responsible for loading the dataset
- **Training**: file responsible for training and saving the model, it's available as a .py format and .ipynb Jupyter notebook format
- **test**: file responsible for loading and testing the model, it's available as a .py format and .ipynb Jupyter notebook format

it contains also 2 main folders:

- **dataset** : contains the dataset in a csv form zipped, make sure to unzip the archive before running the code, downloaded from [here](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv?resource=download)
- **model** : path where your models will be exported, by default it contains 2 trained models, with default parameters, the only difference is the max_iterations, where:
  - logi-reg-100.sav have a max iteration of 100
  - logi-reg-10000.sav have a max iteration of 10000

---

# Installation:

This process is only valid for a native python environment, and not a Conda environment.

## Step 1 Clone the git repo and unzip the dataset

Open terminal, and run the following :

```bash
git clone https://github.com/ZakariyaRguibi/logistic-regression-MNIST.git
```

after that, unzip the dataset so that the mnist_test.csv and mnist_train.csv are in the dataset folder

## Step 2 :Create a python virtual environment

You can either use pip or native python methods

### Using pip (recommended)

#### **Set up pip**

Make sure that pip is already installed by typing the following in your terminal

```bash
pip -h
```

If you see the help text for pip then you have pip installed, otherwise [download and install pip](https://pip.pypa.io/en/latest/installing/)

#### **Install the Virtualenv package**

The Virtualenv package is required to create virtual environments. You can install it with pip:

```bash
pip install virtualenv
```

#### **Create the virtual environment**

To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘.venv’, type the following:

```bash
virtualenv .venv
```

#### **Activate The virtual environment**

You can activate the python environment by running the following command:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### **Using native python**

```bash
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv
```

#### **Activate The virtual environment**

You can activate the python environment by running the following command:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Step 3 :Install required libraries

This project requires Matplotlib, numpy and Scikit-learn libraries, you can install with the following command:

```bash
pip install matplotlib scikit-learn numpy
```

you might need JupyterLab if you want to use Jupyter notebook files

Install JupyterLab with pip:

```bash
pip install jupyterlab
```

Once installed, launch JupyterLab with:

```bash
jupyter-lab
```

for more information about Jupyter, visit [jupyter.org/install](https://jupyter.org/install)

### Step 4 : unzip the dataset

go to dataset folder, and unzip the dataset

# Resources

[Python Virtual Environments](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

# Credit

This repo is created and maintained by Rguibi Zakaria, for ENSA safi 4th year mini project module.

This work is under the [WTFPL](http://www.wtfpl.net/about/) public license
