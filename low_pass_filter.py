from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

b, a = signal.butter(4, 100, 'low', analog=True)
w, h = signal.freqs(b, a)
plt.figure()
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency

t = np.linspace(0, 1, 1000, False)  # 1 second
sig = 5+np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*200*t)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t, sig)
ax1.set_title('10 Hz and 20 Hz sinusoids')
ax1.axis([0, 1, -8, 8])

sos = signal.butter(10, 15, 'low', output='sos', fs = 1000)
filtered = signal.sosfilt(sos, sig)
ax2.plot(t, filtered)
ax2.set_title('After 15 Hz low-pass filter')
ax2.axis([0, 1, -8, 8])
ax2.set_xlabel('Time [seconds]')
plt.tight_layout()

plt.show()
