from scipy.io import wavfile
import numpy as np
import sounddevice as sd
from playsound import playsound
from IPython.display import Audio
import matplotlib.pyplot as plt

# Read in data
Fs, y = wavfile.read('pianonote.wav')
print("The sampling rate is %f" % Fs)  # print out the sampling rate of the audio file
x = y[:, 0]  # two channels are the same, so simply get the first channel
N = x.size  # number of samples
# By checking the data type of x, we see that x is in int16.
# That is each sample of x is represented by 16 bits (i.e. 2 bytes) in signed integer.
# Thus, the range of x is from -32768 to 32767.
# To further process x, we first need to convert it to the  float32 format as follow
x = x/32767


# Perform FFT on the audio signal
X = np.fft.fft(x)

# Shift the zero-frequency component to the center of the spectrum
X = np.fft.fftshift(X)

# Convert the magnitude spectrum to dB scale
Xdb = 20*np.log(np.abs(X))

# Define the frequency axis
freq_axis = np.arange(-N/2, N/2)*(Fs/N)

# Plot the magnitude spectrum
plt.plot(freq_axis, Xdb)

# Label the x-axis and y-axis
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')

# Set the title of the plot
plt.title('Magnitude Spectrum')

# Show the plot
plt.show()

# Set the x-axis limit to -1kHz to 1kHz
plt.plot(freq_axis, Xdb)
plt.xlim(-1000, 1000)
for j in range(-3, 4):
    plt.axvline(j*261.6256,color = 'g',linestyle='dashed')
plt.title('Magnitude Spectrum Limits +-1000kHz')
plt.show()


