from pathlib import Path
import sys
import time
from audioplayer import AudioPlayer
import ctypes
FILEPATH = Path().absolute()

# starts playing music, then minimizes window in 4 seconds, exits when song ends
if __name__ == "__main__":
    playing = AudioPlayer(FILEPATH.__str__() + "\\music\\gravekeeper.mp3")
    playing.play()
    # print("\"ehh... *jams to music*\"")
    print("Now playing...")
    time.sleep(4)
    (ctypes.windll.user32
     .ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6))
    time.sleep(292)
    playing.close()
    sys.exit()
