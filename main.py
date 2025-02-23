from pathlib import Path
import sys
import time
from audioplayer import AudioPlayer
import ctypes
FILEPATH = Path().absolute()

# waits then plays music, minimizes window in 4 seconds, exits when song ends
if __name__ == "__main__":
    time.sleep(5)
    playing = AudioPlayer(FILEPATH.__str__() + "\\media\\gravekeeper.mp3")
    playing.play()
    # print("\"ehh... *jams to music*\"")
    print("Now playing...")
    time.sleep(4)
    # minimize window if windows
    if sys.platform == "win32":
        (ctypes.windll.user32
            .ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6))
    time.sleep(292)
    playing.close()
    sys.exit()
