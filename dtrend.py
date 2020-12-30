from scipy.signal import detrend
from scipy import arange
import matplotlib.pyplot as plt
import numpy as np

seq_no = arange(0, 10, 0.1)
data = np.sin(seq_no) + seq_no *0.2
k = detrend(data)
print (data)
print (k)
print (seq_no)

plt.subplot(121)
plt.plot(seq_no, data)
plt.ylabel("data")
plt.xlabel("seq num")

plt.subplot(122)
plt.plot(seq_no, k)
plt.ylabel("detrended data")
plt.xlabel("seq num")

plt.show()
