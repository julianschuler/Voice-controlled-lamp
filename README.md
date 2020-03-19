# Voice controlled lamp
A voice controlled lamp using the [continuous speech recognition engine julius](https://github.com/julius-speech/julius) and a ESP8266.


## Hardware requirements
- personal computer (your average workstation should be sufficient)
- microphone
- ESP8266 (preferably a developement board like the NodeMCU)
- 5V relay module (those having externel circuitry onboard so they can be driven by a 3.3V signal)
- lamp of your choice, I used 12V high power LEDs, please do yourself a favor and avoid mains!


## Installation
First you need to clone this directory and install julius.
```shell
git clone https://github.com/julianschuler/Voice-controlled-lamp.git
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

Make the scripts executeable.
```shell
chmod +x mic-test.sh voice-control.py./mic-test.sh
```

Now, test if your microphone and the voice detection works by talking to the microphone after starting the script.
```shell
./mic-test.sh
```

To use the python script, the package [pyjulius](https://github.com/Diaoul/pyjulius) is needed, it can be installed using pip (setuptools is needed by pyjulius):
```shell
pip install setuptools 
pip install pyjulius
```

## ESP8266 setup and wiring
Change `STA_SSID` and `STA_PSK` in the file [`lamp-code.ino`](lamp-code/lamp-code.ino) to the WLAN credentials of your home network (important: The PC has to be connected to the same network) und save the modified file. Use the [Arduino IDE](https://www.arduino.cc/en/Main/Software) and the [ESP8266 core](https://github.com/esp8266/Arduino) to upload it to the ESP8266.
The relay module should have three pins on the input side, labeled "IN", "VCC" and "GND" or similar.
Connect "IN" to GPIO14 (D5 for NodeMCU), "VCC" to 5V and "GND" to GND respectively. On the output side search for the normally open (NO) relay contacts, cut one of the power delivering wires of your lamp and hookup the contacts in between.


## Usage
After everything is set up, execute the main script.
```shell
./voice-control.py
```
Wait a few seconds until the startup sequence is done, afterwards the lamp should turn on when saying `lumos` and off when saying `nox`. Note that the first input will be used for normalisation und thus always be discarded.


## License
This project is licensed under the MIT license, see [`LICENSE.txt`](LICENSE.txt) for further information.
