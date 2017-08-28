# HC05 Bluetooth Communication between Arduino Uno and Raspberry Pi 3
To create bluetooth connection, we need to do 3 things:

1. Wire the Bluetooth Module to our Arduino and enter AT+Commands to ensure everything is configured properly
2. Ensure bluetooth connectivity is available on the Raspberry Pi and successfully connect to the Bluetooth Module powered by the Arduino
3. Create a script on the Raspberry Pi to listen to and respond to Bluetooth Serial communication.

**NOTE: Watch this video for more information, and for an explanation for why I chose the HC-05 over the HM10 knock-off**
[Video: Arduino and Raspberry Pi Communication](https://www.youtube.com/watch?v=rnuwRSg_uRA&lc=z23atfo5vzndepyxv04t1aokgmi5e4jk1yjotohtn2zjbk0h00410)

# Step 1: Setup Arduino #
You can find my Arduino Code and the fritzing wiring diagram [here](https://create.arduino.cc/editor/jweston/3dbd933f-5a90-4fa9-82c4-6ebc5d4ae3c7/preview)

Information about HC05 accessing AT+Commands on HC05:

* We do not need the state pin
* Do not connect the VCC. Upload your sketch, hold the button on the module, then plug in the VCC. You should be in AT mode.
* Advertised as 9600 BAUD rate but really 38400 when using AT Mode this way
* This is considered “mini AT Mode” and certain commands are not available.
* To use all of the commands, you either need the Arduino to control the module, or you can hold the button in while sending a command (easier method)

* HC-05 commands are different that BLE CC41a (HM10 knockoff). Here is a table of commands:

![HC05 AT](https://github.com/Josh-Weston/ArduinoRPi/blob/master/HC05.png)

# Step 2: Setup bluetooth communication on Raspberry Pi #




# Step 3: Setup Raspberry Pi to listen and respond to Bluetooth messages #




**Connect RFCOMM**
`sudo rfcomm connect hci0 98:D3:32:20:82:9D 1`

**Release RFCOMM**
`sudo rfcomm release 0`

**Evernote notes for RPi Bluetooth**
https://www.evernote.com/l/APYYp-XLKYdPXri9bdpeInmNhQ3HudtNwuo

**Evernote notes for HC05 AT+Mode and connections**
https://www.evernote.com/l/APYiL7KLZOtKGY6tOc38yGRrSc4Zzerorsk

**Arduino Code and wiring diagram** https://create.arduino.cc/editor/jweston/3dbd933f-5a90-4fa9-82c4-6ebc5d4ae3c7/preview

