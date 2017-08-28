# HC05 Bluetooth Communication between Arduino Uno and Raspberry Pi 3
To create bluetooth connection, we need to do 3 things:

1. Wire the Bluetooth Module to our Arduino and enter AT+Commands to ensure everything is configured properly
2. Ensure bluetooth connectivity is available on the Raspberry Pi and successfully connect to the Bluetooth Module powered by the Arduino
3. Create a script on the Raspberry Pi to listen to and respond to Bluetooth Serial communication.

**NOTE: Watch this video for more information, and for an explanation for why I chose the HC-05 over the HM10 knock-off**
[Video: Arduino and Raspberry Pi Communication](https://www.youtube.com/watch?v=rnuwRSg_uRA&lc=z23atfo5vzndepyxv04t1aokgmi5e4jk1yjotohtn2zjbk0h00410)

# Step 1: Setup Arduino #
You can find my Arduino Code and the fritzing wiring diagram [here](https://create.arduino.cc/editor/jweston/3dbd933f-5a90-4fa9-82c4-6ebc5d4ae3c7/preview)


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

