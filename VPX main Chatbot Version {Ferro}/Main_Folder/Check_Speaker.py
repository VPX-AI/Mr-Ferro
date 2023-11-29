import banner , Const_Vari

import warnings
from pydub import AudioSegment
from pydub.playback import play

print(Const_Vari.Line_Break*2)
banner.Ferro_Sound_Banner()
print(Const_Vari.Line_Break*2)

try:
    silent_segment = AudioSegment.silent(duration=100)
    play(silent_segment)
    Speakers_Connected = True
    print(Const_Vari.Line_Break)
    print("Speaks are Connected. So There Will be some Sound, If Speakes Are not Connected Then Also its Show Error then Tell This to Head Of Project By going to \"https://linksly.co/7al8xVi\"")
    print(Const_Vari.Line_Break)
except Exception as e:
    Speakers_Connected = False
    print(Const_Vari.Line_Break)
    print("No Speaks Connected. So No Sound, If Speakes Are Connected Then Also its Show Error then Tell This to Head Of Project By going to \"https://linksly.co/7al8xVi\"")
    print(Const_Vari.Line_Break)
