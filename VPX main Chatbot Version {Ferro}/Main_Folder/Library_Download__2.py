"""
_____________________________________________________________________________________________
Source code of VPX-AI by Company VPX {Owner=>Vikrant Pathania}
Welcome All To This Source code of Chating Part Of AI Module == {Ferro} 
Developers => {||__|| => 100% <= ||__||} VIKRANT PATHANIA  ~ MrFerro , VP , MrCaffene
Starting On => 2-11-2023
_____________________________________________________________________________________________
"""
#_________________________________________Starting_________________________________________#
#__________________________________________LibRary________________________________________#


import subprocess
import os
import time
import pyautogui
import sys

System_Message = "| ~ | System | ~ | =========> "
Space = """


"""
Arrow = "==>"

def Close_Program():
    pyautogui.FAILSAFE = False
    screen_width, screen_height = pyautogui.size()
    target_x = screen_width
    target_y = 0
    pyautogui.moveTo(target_x, target_y, duration=0.35)
    time.sleep(0.4)
    pyautogui.click()
    target_x = -500
    target_y = 500
    pyautogui.move(target_x,target_y,duration=0.35)
    time.sleep(0.1)
def play_mp3(file_path):
    subprocess.Popen(['start', '', file_path], shell=True, startupinfo=subprocess.STARTUPINFO(), creationflags=subprocess.CREATE_NO_WINDOW)
def animated_hash():
    for _ in range(260):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(0.02)
def install_or_update_libraries():
    libraries = ["pyaudio","playsound","pyttsx3"]
    for library in libraries:
        print(f"{Space}{System_Message}Installing or updating {library}...{Space}")
        subprocess.run(f"pip install --upgrade {library}", shell=True)
    print(f"{Space}{System_Message}Installation/update complete.{Space}")
def System_Sound():
    script_path = os.path.abspath(__file__)
    mp3_path = os.path.join(os.path.dirname(script_path), "Sounds", "System.mp3")
    play_mp3(mp3_path)
    time.sleep(2.5)
    Close_Program()

install_or_update_libraries()
System_Sound()
file_two_path = 'Main_BOT.py'
subprocess.run(['python', file_two_path])
sys.exit()