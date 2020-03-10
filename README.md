# Voice controlled lamp
A voice controlled lamp using the [continuous speech recognition engine julius](https://github.com/julius-speech/julius) and a Raspberry Pi.
Note: This project is still in the test and setup progress, thus not fully functional yet.


## Hardware requirements
- Raspberry Pi (version shouldn't matter, tested with a Raspberry Pi 2B)
- USB microphone
- Rasperry Pi accessories (SD card, power supply, possibly adapters)


components needed for testing, will be replaced in the future:
- LED
- current limiting resistor (~1kΩ)
- female jumper cables
- breadboard


## Wiring
Use the female jumper cables and the bradboard to connect the anode of the LED through a 1kΩ resistor to pin BCM 27 (physical pin 13) and its cathode to ground.


## Installation
First, install a version of Raspian on the Pi and disable booting to dektop (e.g. by using `raspi-config`). Clone this repository into the home folder on the Pi and execute the following commands to install julius:
```shell
cd Voice-controlled-lamp
git submodule update --init
sudo apt install build-essential zlib1g-dev libsdl2-dev libasound2-dev
cd julius
./configure --enable-words-int
make -j4
```

Now you need to download the english DNN language model and unzip it.
```shell
cd ..
wget https://sourceforge.net/projects/juliusmodels/files/ENVR-v5.4.Dnn.Bin.zip
unzip ENVR-v5.4.Dnn.Bin.zip
```

Optionally, you can now remove the zip archive, since it is not needed anymore.
```shell
rm ENVR-v5.4.Dnn.Bin.zip
```

Now, test if your microphone and the voice detection works by simply talking to the microphone after starting the script.
```shell
./mic-test.sh
```

To use the python script, the package [pyjulius](https://github.com/Diaoul/pyjulius) is needed, it can be installed using pip (setuptools is needed by pyjulius):
```shell
pip install setuptools 
pip install pyjulius
```

Finally, start julius, switch to another terminal (Ctrl-Alt-F2) and start the voice control there, afterwards the system is ready to use.
```shell
./start.sh
```


## Usage
After everything is set up, the LED/lamp should turn on when saying `lumos` and off when saying `nox`.


## License
This project is licensed under the MIT license, see [`LICENSE.txt`](LICENSE.txt) for further information.
