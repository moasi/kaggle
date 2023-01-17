#llibreries a utilitzar
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import svm
from sklearn.metrics import accuracy_score, recall_score
import time
import seaborn as sns
import cv2
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.losses import sparse_categorical_crossentropy
from keras.optimizers import Adam
from sklearn.model_selection import KFold
from keras.utils import to_categorical



def crear_labels(TRAIN_PATH):
    labels = []
    imnames = []
    imlabels = []
    for class_ in os.listdir(TRAIN_PATH):
        labels.append(class_)
        for im in os.listdir(TRAIN_PATH+str(class_)):
            imnames.append(TRAIN_PATH+str(class_)+"/"+str(im))
            imlabels.append(class_)
    NUM_LABELS = len(labels)
    NUM_IMG = len(imlabels)

    return labels,imlabels,imnames,NUM_LABELS,NUM_IMG
