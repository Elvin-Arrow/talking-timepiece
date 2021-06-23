# Talking timepiece
A small script that says time aloud when run.
 
To get it to work:
- [pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
- playsound
- gTTS

## Install pyaudio on Linux

1. First run the following command in terminal 
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```
2. Then run
```bash
pip install pyaudio
```

## Troubleshooting
**In case of a `'gi' module not found` error use the following commands**

The simple way:

```bash
sudo apt-get install python3-gi
```

or

For virtualenv users - The vext way

```bash
pip install vext

pip install vext.gi
```

The pure python developer way:

Install a bunch of developer stuff:

```bash
sudo apt-get install pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev
```

Install the python packages:

```bash
pip install gobject PyGObject
```
