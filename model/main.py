import numpy as np
from scipy import signal, datasets
import matplotlib.pyplot as plt
import pandas as pd

data_fft = pd.read_csv('sensor_1.csv')
y = np.array(data_fft.AEP_MW)
x = data_fft.index
date_array = pd.to_datetime(data_fft.Datetime)
plt.plot(date_array,y)
plt.xlabel('time',fontsize=20)
plt.ylabel('sensor',fontsize=20)