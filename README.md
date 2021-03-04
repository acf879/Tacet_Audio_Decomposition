# Tacet_Audio_Decomposition
Decompose .wav files using fourier transform into individual amplitudes and frequencies per time step. Various test files are included to make sure it is configured correctly. Following the finished program a name of the file ( if file not in same folder use path ) will be entered and once convert in the gui has been pressed will close the gui and run the program. The program will open the file and perform a fourier transform for individual pieces of the provided file making a notepad with an amplitude and a frequency with each line corresponding to each time step with size of time step being on the first line.
Example of finished project:

1ms
5.01 5021 
4.30 4542
5.65 345

This will continue for the entire .wav file with the first element of the line corresponding to the amplitude and the second the frequency of the file.
