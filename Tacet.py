# Import modules

import tkinter as tk
from scipy.io import wavfile
import scipy
import scipy.fftpack as fftpk
from matplotlib import pyplot as plt
import wave


def fft_on_audio(audio_path):
    """
    Purpose: To deconstruct an audio file into its amplitudes and frequencies.
    :param audio_path: Audio file to perform fft on
    :return: amplitude (ampl) and frequency (freq)
    """
    samp_rate, signal = wavfile.read(audio_path)
    amplitude = abs(scipy.fft.fft(signal))
    freq = fftpk.fftfreq(len(amplitude), 1/samp_rate)
    return amplitude, freq


def plot_fft(audio_file):
    """
    Purpose: To plot the fourier transform for particular audio file
    :param audio_file: Path to the audio file to perform the decomposition for
    Return: True if the function was called correctly
    """
    if audio_file[-4:] == '.wav':
        ampl, freqs = fft_on_audio(audio_file)
        plt.plot(freqs, ampl)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
        plt.show()
        return True
    return False


class Audio:
    def __init__(self, filename):
        self.__filename = filename
        self.__audio = wave.open(self.__filename)
        self._sample_rate, self._signal = wavfile.read(filename)

    def duration(self):
        """
        Purpose: To determine the length of the audio
        :return: length of audio
        """
        return len(self.__audio)

    def split(self, ti, tf, new_file):
        """
        Purpose: To divide the audio file into smaller files to perform the fft on. Time is in seconds
        Pre-conditions
            :param ti: Beginning of sampling time
            :param tf: End of sampling time
            :param new_file: Name of new audio file to be produced for the length of time
        :return: True if performed correctly, false otherwise
        """
        if new_file[-4:] == '.wav':
            tf *= 1000
            ti *= 1000
            file = open(new_file, 'a')
            file.close()
            wavfile.write(new_file, self._sample_rate, self._signal[ti:tf])
            return True
        return False

    def get_audio(self):
        """
        Purpose: To return the audio in its array form
        :return: audio array
        """
        return self.__audio

    def get_filename(self):
        """
        Purpose: To return name of audio file
        :return: Returns audio file name
        """
        return self.__filename


class Application:
    def __init__(self):
        self._file_path = ''  # default audio file to overwrite with correct file
        app = tk.Tk(className="Tacet Application")
        app.geometry('150x60')  # size of default widget without being resized
        app_entry = tk.Entry(master=app, text='Enter file path')  # textbox to enter file path
        scrollbar = tk.Scrollbar(master=app, orient=tk.HORIZONTAL)
        scrollbar.config(command=app_entry.xview)
        scrollbar.pack(side='top', fill='x')
        app_entry.config(xscrollcommand=scrollbar.set)
        app_entry.pack()
        button = tk.Button(master=app, text='Convert', width=17, height=1, command=lambda: self.set(app_entry.get()))
        button.pack(side='bottom')

    def set(self, entry=''):
        """
        Purpose: To set the file path from the button widget
        :param entry: File path to save
        """
        self._file_path = entry

    def get(self):
        """
        Purpose: To obtain the file path from the button widget
        :return: file path from button widget
        """
        return self._file_path

    def fft_plot(self):
        """
        Purpose: To perform and plot an fft of a particular audio file
        :return: True if function works properly
        """
        plot_fft(self._file_path)
        return True
    
    def audio_fft(self):
        """
        Purpose: To perform the fft on an audio file
        :return: To return the fft of a particular audio file
        """
        return fft_on_audio(self._file_path)
    
    def audio_sampling(self, sampling_rate):
        """
        Purpose: To create temporary .wav files without affecting the input file
        :param: sampling_rate: The rate that the audio file is sampled
        :return: None
        """
        pass


app = Application
app()

audio = Audio('test2.wav')
audio.split(30, 60, 'test10.wav')
plot_fft('test2.wav')
