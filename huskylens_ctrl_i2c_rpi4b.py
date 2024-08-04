from huskylib1 import HuskyLensLibrary
from enum import Enum
import time
import subprocess


#This example control the Huskylens via I2C of the Raspberry Pi 4B
#The firmware version of the Huskylens is 0.5.1aNorm when this example is written

# Enable I2C Interface
#    Run sudo raspi-config and navigate to "Interfacing Options" > "I2C"
#       Select "Yes" to enable I2C and "Yes" to load the kernel module
#       Select "Finish" and reboot when prompted

# Install the necessary Python libraries for I2C:
#    sudo apt-get install python3-smbus python3-dev

# Install eSpeak (this is the Text to Speech)
#    sudo apt-get install espeak

HANDSHAKE_CONFIRM_COUNT = 3
VOICE_ANNOUNCEMENT_ENABLE = True

# Enumeration that matches the previously learned object classification in the Huskylens
class myLearntObjID(Enum):
    OBJ_ID_METAL = 1
    OBJ_ID_PAPER = 2
    OBJ_ID_PLASTIC = 3
    

# This function check if all the element in the array are same value
def all_elements_same(arr):
    return all(x == arr[0] for x in arr)

# This function produce voice annoucement using Text to Speech
def speak(text):
    if(VOICE_ANNOUNCEMENT_ENABLE==True):
        subprocess.call(['espeak', text])

# This function carries out further action once the object is detected.
#   For example, user could control movement of motor, flashing LED, etc.
#      In this example, the object classification has been "learned" accordingly
#      as per the enumeration table
def take_action(id_detected):
    match id_detected:
        case myLearntObjID.OBJ_ID_METAL.value:
            txt_metal = "Metal"
            print(txt_metal)
            speak(txt_metal)
            #ToDo: other action could be added here, e.g. move a motor,
            #        update display, flashing LED, etc.
        case myLearntObjID.OBJ_ID_PAPER.value:
            txt_paper = "Paper"
            print(txt_paper)
            speak(txt_paper)
            #ToDo: other action could be added here, e.g. move a motor,
            #        update display, flashing LED, etc.
        case myLearntObjID.OBJ_ID_PLASTIC.value:
            txt_plastic = "Plastic"
            print(txt_plastic)
            speak(txt_plastic)
            #ToDo: other action could be added here, e.g. move a motor,
            #        update display, flashing LED, etc.
        case _:
            txt_unknown = "unknown"
            print(txt_unknown)
            speak(txt_unknown) 
            #ToDo: other action could be added here, e.g. move a motor,
            #        update display, flashing LED, etc.   

def cfgHuskyLens():
    txt_hs = "Attempt handshaking with Husky Lens"
    print(txt_hs)
    speak(txt_hs)
    _huskyLens = HuskyLensLibrary(proto="I2C",comPort="",address=0x32)
    handshake_debounce_count = HANDSHAKE_CONFIRM_COUNT
    while(handshake_debounce_count>0):
        if(_huskyLens.knock()=="Knock Recieved"):
            handshake_debounce_count -= 1
            time.sleep(0.2)
        else:
            handshake_debounce_count = HANDSHAKE_CONFIRM_COUNT
            txt_fail_hs = "Fails to discover Husky Lens, please check connection or setting"
            print(txt_fail_hs)
            speak(txt_fail_hs)
            time.sleep(2)    
            print(txt_hs)
            speak(txt_hs)
    if(handshake_debounce_count<=0):
        text = "Husky Lens detected"
        print(text)
        speak(text)        
        _huskyLens.algorthim("ALGORITHM_OBJECT_CLASSIFICATION")
        time.sleep(1)
        return _huskyLens

def mainCtrl(_obj_hl):
    OBJECT_DETECTION_DEBOUNCE_COUNT = 3
    OBJECT_DETECTION_DEBOUNCE_DURATION = 0.2
    while True:
        #print(huskyLens.learnedObjCount())
        #time.sleep(0.5)
        _dataObj = _obj_hl.blocks()
        if(_dataObj):
            print(_dataObj.getID())
            #obtain the object ID detected from HuskyLens
            _object_id = _dataObj.getID()
            if _object_id > 0: #something valid is detected!!!
                detected_obj_id = [0,0,0]
                for i in range(OBJECT_DETECTION_DEBOUNCE_COUNT):
                    time.sleep(OBJECT_DETECTION_DEBOUNCE_DURATION)
                    _data_Obj= _obj_hl.blocks()
                    print(_data_Obj.getID())
                    detected_obj_id[i] = _data_Obj.getID()
                print(detected_obj_id)
                if(all_elements_same(detected_obj_id)):
                    take_action(detected_obj_id[0])
                else:
                    print("try again")
            else:
                print("invalid object ID")

#--------------------------------------------------------------------------------------------
# Starts here
#--------------------------------------------------------------------------------------------

# Indicating program starts
speak("Welcome")
time.sleep(0.5)
# begins with configuration
objHL = cfgHuskyLens()
if(objHL):
    mainCtrl(objHL)
else:
    speak("Program ended, thank you")    


