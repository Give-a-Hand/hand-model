from scipy.stats import kurtosis, skew
import numpy as np


arr = np.array([1, 2, 3, 4, 5]) # set arr as some dataset

def calculate_mean(arr):
    return np.mean(arr)

def calculate_std(arr):
    return np.std(arr)

def calculate_first_quart(arr):
    return np.percentile(arr, 25)

def calculate_third_quart(arr):
    return np.percentile(arr, 75)

def calculate_kurtosis(arr):
    kurtosis = kurtosis(arr, axis=0, bias=True)
    return kurtosis

def calculate_skewness(arr):
    skewness = skew(arr, axis=0, bias=True)
    return skewness