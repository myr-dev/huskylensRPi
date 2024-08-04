# huskylensRPi
This is a Python project to control the Huskylens using the Raspberry Pi 4B I2C interface


This example control the Huskylens via I2C of the Raspberry Pi 4B
The firmware version of the Huskylens is 0.5.1aNorm when this example is written

Enable I2C Interface
    Run sudo raspi-config and navigate to "Interfacing Options" > "I2C"
       Select "Yes" to enable I2C and "Yes" to load the kernel module
       Select "Finish" and reboot when prompted

Install the necessary Python libraries for I2C:
    sudo apt-get install python3-smbus python3-dev

Install eSpeak (this is the Text to Speech)
    sudo apt-get install espeak
