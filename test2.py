from ctypes import *
import time
import ctypes
import clr
import sys

p = ctypes.cdll.LoadLibrary("PTZ.dll")

from PTZ import PTZDevice, PTZType
print PTZType.Relative

# This will work only for logitech c920 camera, For a specific camera, You have
# pass the camera model name in below function. 
b = PTZDevice.GetDevice('Logitech HD Pro Webcam C920', PTZType.Absolute)

# Here in Zoom() you can pass the integer negative or positive value.
b.Zoom(2)
# or b.Zoom(-10)

# This will control pan and tilt of camera, This will not work for logitechc920,
# because it doesn't support this feature, so i have passed PTZType.Absolute in 
# GetDevice function.

# Logitech orbit/sphere supports Pan and tilt. You have to pass PTZType.Relative
# in above GetDevice function.
b.Move(30,10)
