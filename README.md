# HC05 Bluetooth Communication between Arduino Uno and Raspberry Pi 3
To create bluetooth connection, we need to do 3 things:

1. Wire the Bluetooth Module to our Arduino and enter AT+Commands to ensure everything is configured properly
2. Ensure bluetooth connectivity is available on the Raspberry Pi and successfully connect to the Bluetooth Module powered by the Arduino
3. Create a script on the Raspberry Pi to listen to and respond to Bluetooth Serial communication.

**NOTE: Watch this video for more information, and for an explanation for why I chose the HC-05 over the HM10 knock-off**
[Video: Arduino and Raspberry Pi Communication](https://www.youtube.com/watch?v=rnuwRSg_uRA&lc=z23atfo5vzndepyxv04t1aokgmi5e4jk1yjotohtn2zjbk0h00410)

**Disclaimer: A lot of trial-and-error went into establishing the connection, so these steps may not be 100% complete; however, they are materially accurate, and should provide enough guidance to troubleshoot issues you encounter.**

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
This part can be really easy or tricky depending on your setup. If you are using a Raspberry Pi 3, you will already have a graphical Bluetooth interface that can help with this step. There are 3 things to remember:

1. You need to know the MAC Address of your Bluetooth Module
2. You need to pair to the Bluetooth Module
3. You need to open an RFCOMM channel so Raspberry Pi knows it should be communicating. It is not enough to simply pair the devices, you need an RFCOMM channel open.

If you are using the graphical interface, you should be able to find your device and locate its unique MAC address. It will look something like: 98:D3:32:20:82:9D

If you do not have the graphical interface, or are having problems you can follow these steps:

* Type `sudo bluetoothctl` into a terminal and input the admin password if prompted
* Type `agent on` and press enter. Then type `default-agent` and press enter.
* Type `scan on` and the raspberry pi will scan for broadcasting Bluetooth devices nearby.
* Type `pair 98:D3:32:20:82:9D` replacing the MAC Address with that of your bluetooth module
* Type `info 98:D3:32:20:82:9D` to see information about the device.

Once you have successfully paired the bluetooth module to your Raspberry Pi, you will need to bind to an RFCOMM channel before they can communicate:

1. `sudo rfcomm bind hci0 98:D3:32:20:82:9D 1` will bind the bluetooth device to the RPi bluetooth module
2. `sudo rfcomm release 0` will release the bluetooth module from rfcomm0


# Step 3: Setup Raspberry Pi to listen and respond to Bluetooth messages #
The Raspberry Pi code I used can be found in this [here.](https://github.com/Josh-Weston/ArduinoRPi/blob/master/HC05_bluetooth_read.py)


