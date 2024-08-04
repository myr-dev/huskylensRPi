# huskylensRPi
This is a Python project to control the Huskylens using the Raspberry Pi 4B I2C interface


This example control the Huskylens via I2C of the Raspberry Pi 4B
The firmware version of the Huskylens is 0.5.1aNorm when this example is written

This example attempts to demonstrate the communication with Huskylens via the I2C interface.

The Huskylens is first set into object classification mode and learned to detect three type of object.
Namely a metal can, a plastic bottle and a paper box.
Huskylens is assigned each object with an ID number.

The Python program is then retrieve the detected object ID from the Huskylens,
and then associate the detected ID with its type (e.g. Metal), and play the respective
Text-to-Speak.

-----------------------------------------------------
Pin out 
-----------------------------------------------------
(Please refer to the documentation of Huskylens and Raspberry Pi respectively)

Huskylens:
T = SDA,
R = SCL

Raspberry Pi 4B:
Pin 3 = SDA,
Pin 5 = SCL

-----------------------------------------------------
Prerequisite:
-----------------------------------------------------
The Python version used for this example is Python3.

Enable I2C Interface
    Run sudo raspi-config and navigate to "Interfacing Options" > "I2C"
       Select "Yes" to enable I2C and "Yes" to load the kernel module
       Select "Finish" and reboot when prompted

Install the necessary Python libraries for I2C:
    sudo apt-get install python3-smbus python3-dev

Install eSpeak (this is the Text to Speech)
    sudo apt-get install espeak

The Huskylens library could be obtained from 
https://github.com/HuskyLens/HUSKYLENSPython    
(a slight modification of the huskylib for this example:
    a function to getID is being added into the block class)
    
--------------------------------------------------
Flow of program
--------------------------------------------------
1. Attempt to establish communication with Huskylens
2. If successful, configure the Huskylens to perform Object Classification
3. For each detected object ID, play voice annoucement via Text to Speech
    
