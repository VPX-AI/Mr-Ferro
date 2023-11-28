import warnings
from pydub import AudioSegment
from pydub.playback import play

warnings.filterwarnings("ignore", message="Couldn't find ffmpeg or avconv")

try:
    silent_segment = AudioSegment.silent(duration=100)
    play(silent_segment)
    Speakers_Connected = True
except Exception as e:
    Speakers_Connected = False
    print(f"Error: {e}")