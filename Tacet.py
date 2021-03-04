import tkinter as tk

from scipy.io import wavfile as wavefile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt

audio_file_raw = ''

# Making sudo const

class constant():
    def __init__(self, value = ''):
        self.__const = value

    def set(self, value):
        self.__const = value
    def get(self):
        return self.__const

# Making the GUI

app = tk.Tk(className='Tacet Application')
app.geometry('200x80')

audio_file_entry = tk.Entry(master = app, text = 'Enter name of file')

scrollbar = tk.Scrollbar(master=app, orient=tk.HORIZONTAL)
scrollbar.config(command=audio_file_entry.xview)
scrollbar.pack(side='bottom', fill='x')
audio_file_entry.config(xscrollcommand = scrollbar.set)
audio_file_entry.pack()

audio_file = constant()


recieving_button = tk.Button(master=app, text = 'Convert', width = 17, height = 1, command=lambda : audio_file_recieving())  # Creates button to send in to program for opening
recieving_button.pack()

# File input and preprocessing

def audio_file_recieving():
    """
    Purpose:
        To extract the audio file from the tkinter widget
    Post-conditions:
        Changes gloal var audio_file to corresponding input
    """
    audio_file.set(audio_file_entry.get())  # Sets the variable to the value in the widget

    try:
        file = open(audio_file.get(), 'r')  # Tries to open the file to check if it is valid
        file.close()
    except:
        print('invalid input: Not .wav file or unable to locate')
    global audio_file_raw
    audio_file_raw = audio_file.get()

app.mainloop()  # Loops program to allow for real time interaction

# FFT on audio file: Decomposes the audio file into amplitudes and frequencies
s_rate, signal = wavefile.read(audio_file_raw)
FFT = abs(scipy.fft.fft(signal))
freqs = fftpk.fftfreq(len(FFT),(1.0/s_rate))


plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

""" Still needs times to show timing on audio file and convert from decimals to binary """

# Write digital signal to text file
    # Output text in (# of motors, frequency) lines will simulate time steps
file_wr = open('Output.txt','w')
# Add frequency and amplitude to each line 
# Have lines correspond to time steps 

