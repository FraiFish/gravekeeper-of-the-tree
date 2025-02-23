from pathlib import Path
import sys
import time
from audioplayer import AudioPlayer
FILEPATH = Path().absolute()

if __name__ == "__main__":
    playing = AudioPlayer(FILEPATH.__str__() + "\\music\\gravekeeper.mp3")
    playing.volume = 75  # it was a bit too loud
    playing.play()
    print("Now playing...")
    input()
    time.sleep(296)
    playing.close()
    sys.exit()
