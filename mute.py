#import tk 
#from tk import * 
#root=Tk()
#import tkSnack
import time
#import mute
import datetime
from sound import Sound
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math


#root = Tkinter.Tk()
#tkSnack.initializeSnack(root)
#root.withdraw()

def Mute(seconds):
    #global original
    #original = tkSnack.audio.play_gain()
    #tkSnack.audio.play_gain(0)
    Sound.mute()
    delta = datetime.timedelta(days=0, hours=0, minutes=0, seconds=seconds)
    while datetime.datetime.now() < delta:
        time.sleep(1)
    #tkSnack.audio.play_gain(original)
    Sound.mute()
    #if boolean is True:
    #    original = tkSnack.audio.play_gain()
    #    print "the original before mute is:", original
    #    tkSnack.audio.play_gain(0)
    #    
    #elif boolean is False:
    #    g = globals()
    #    if (tkSnack.audio.play_gain() == 0) and (g.has_key('original')):
    #        tkSnack.audio.play_gain(original)
    #    elif tkSnack.audio.play_gain() == 0:
    #        tkSnack.audio.play_gain(100)
    #    else:
    #        pass

if __name__ == '__main__':
    #quit = 0
    #global original
    #original = tkSnack.audio.play_gain()
    #mute.Mute(30)
    Sound.mute()
    #delta = datetime.datetime(year=0,month=0,day=0, hour=0, minute=0, second=10)
    time.sleep(75)
    # Get default audio device using PyCAW
    Sound.mute()
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(currentVolumeDb - 20.0, None)
    # NOTE: -6.0 dB = half volume !
    #tkSnack.audio.play_gain(original)
    #Sound.volume_down()
    #Sound.__set_current_volume(30)
    #while quit == 0:
    #    print "(1) Mute Sound"
    #    print "(2) Unmute Sound"
    #    print "(3) Quit"
    #    choice = input("Choice: ")
    #    mute.Mute(30)
    #    if choice == 1:
    #        mute.Mute(True)
    #    elif choice == 2:
    #        mute.Mute(False)
    #    elif choice == 3:
    #        break
    #    else:
    #        print "You have made an invalid selection"