# Talking timepiece
A small script that says time aloud when run.
 
To get it to work:
- [pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
- playsound
- gTTS

## Install pyaudio on Linux
1. First we need to install portaudio modules: ```sudo apt-get install libasound-dev```

2. Download the portaudio archive from: http://portaudio.com/download.html

2. Unzip the archive: tar -zxvf [portaudio.tgz]

3. Enter the directory, then run: ```./configure && make```

4. Install: ```sudo make install```

5. And finally: ```pip install pyaudio```