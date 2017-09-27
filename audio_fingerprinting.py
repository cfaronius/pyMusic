from scipy.io import wavfile
from scipy.fftpack import fft
from matplotlib import pyplot as plt
import numpy as np

def printf(format, *values):
    print(format % values )

# Load the data and calculate the time of each sample
samplerate, data = wavfile.read('063-Shakira_-_Try_Everything.wav')
times = np.arange(len(data))/float(samplerate)
printf("samplerate %d", samplerate)

fft_out = fft(data)

# Make the plot
# You can tweak the figsize (width, height) in inches
plt.figure(1, figsize=(30, 4))
plt.plot(data)
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.show()

plt.figure(2, figsize=(30, 4))
plt.plot(fft_out)
plt.show()
