from pathlib import Path
import sys
import time
from audioplayer import AudioPlayer
import ctypes

FILEPATH = Path().absolute()

"""
Waits 3 seconds, plays the song, and then closes
If the system running the script is windows, minimize the terminal running it 
4 seconds after the song has started playing
"""
if __name__ == "__main__":
    print("Starting...")
    time.sleep(3)
    playing = AudioPlayer(FILEPATH.__str__() + "\\media\\gravekeeper.mp3")
    playing.play()
    # print("\"ehh... *jams to music*\"")
    time.sleep(4)
    # minimize window if windows
    if sys.platform == "win32":
        (ctypes.windll.user32
            .ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6))
    time.sleep(292)
    playing.close()
    sys.exit()
