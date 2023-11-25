"""
_____________________________________________________________________________________________
Source code of VPX-AI by Company VPX {Owner=>Vikrant Pathania}
Welcome All To This Source code of Chating Part Of AI Module == {Ferro} 
Developers => {||__|| => 100% <= ||__||} VIKRANT PATHANIA  ~ MrFerro , VP , MrCaffene
Starting On => 2-11-2023
_____________________________________________________________________________________________

"""
#_________________________________________Starting_________________________________________#
#_________________________________________Main Code________________________________________#

#Librarys {Self}

import BOT_Input , BOT_Output

#Librarys {Taken}

import pyaudio
import random
import webbrowser
import pyttsx3
import sys
import time

#All Functions

##def process_user_input(user_input):
    ##return f'This is the response to: {user_input}'
def Animation_Of_Tilt():
    for _ in range(139):
        sys.stdout.write("~")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_UnderScore():
    for _ in range(139):
        sys.stdout.write("_")
        sys.stdout.flush()
        time.sleep(0.001)
def check_speaker_connection():
    global num_devices, speaker_connected, volume , speech_rate
    speaker_connected = False
    p = pyaudio.PyAudio()
    try:
        num_devices = p.get_device_count()
        if num_devices > 0:
            Animation_Of_Tilt()
            print("Speakers are connected to your computer.")
            Animation_Of_UnderScore()
            print("Checking all other devices connected to your computer:")
            Animation_Of_UnderScore()
            speaker_connected = True
            for i in range(num_devices):
                device_info = p.get_device_info_by_index(i)
                if device_info['maxOutputChannels'] > 0:
                    print(f"Device {i}: {device_info['name']}")
        else:
            Animation_Of_Tilt()
            print("No speaker is Not connected. Volume is set to 0.")
            Animation_Of_Tilt()
            speaker_connected = False
            volume = 0
            speech_rate = 0
    except Exception as e:
        print(f"An error occurred: {e}")
        speaker_connected = False
        volume=0
        speech_rate = 0
def Volume_And_Speech():
    global Volume_Applied , volume
    speaker_connected = True

    if speaker_connected:
        volume = int(input("Please Enter The Volume You Want to Add ===> "))
        if 0 < volume <= 100:
            print(f"Volume Is Applied To ===> {volume}")
            Volume_Applied = True
        elif not (0 < volume <= 100):
            print(f"""Hey User, You Have Applied Volume To {volume}
This Amount Of Volume Is Not Valid, So I Set the Default Volume to '100'""")

def speak(text):
    Text_To_Speech_Lib.say(text)
    Text_To_Speech_Lib.runAndWait()
def Animation_Ferro_Banner_Sound():
    for _ in range(139):
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.001)
    for _ in range(139):
        sys.stdout.write("\\")
        sys.stdout.flush()
        time.sleep(0.001)
    for _ in range(139):
        sys.stdout.write("/")
        sys.stdout.flush()
        time.sleep(0.001)
    for _ in range(139):
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Ferro_Banner():
    for _ in range(139):
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.001)
    for _ in range(139):
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.001)
def Ferro_Sound():
    Animation_Ferro_Banner_Sound()
    print(""" 
    
                                 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  
                                ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌ 
                                ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
                                ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
                                ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
                                ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
                                 ▀▀▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
                                          ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
                                 ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
                                ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌ 
                                 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  
            """)
    Animation_Ferro_Banner_Sound()        
def Ferro_Banner():
    print("")
    Animation_Ferro_Banner()
    print(""" 
    
                |  ~  |         ███╗   ███╗██████╗     ███████╗███████╗██████╗ ██████╗   ██████╗           |  ~  |
                |  ~  |         ████╗ ████║██╔══██╗    ██╔════╝██╔════╝██╔══██╗██╔══██╗ ██╔═══██╗          |  ~  |
                |  ~  |         ██╔████╔██║██████╔╝    █████╗  █████╗  ██████╔╝██████╔╝ ██║   ██║          |  ~  |
                |  ~  |         ██║╚██╔╝██║██╔══██╗    ██╔══╝  ██╔══╝  ██╔══██╗██╔══██╗ ██║   ██║          |  ~  |
                |  ~  |         ██║ ╚═╝ ██║██║  ██║    ██║     ███████╗██║  ██║██║  ██║ ╚██████╔╝          |  ~  |
                |  ~  |         ╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═════╝           |  ~  |

            """)
    Animation_Ferro_Banner()
    print("")
def BOT_EXIT_Review():
    EXP = input("""This Bot is Made By Vikrant Pathania, a School Student of 16 years.
He made this using 100% Python, random, and webbrowser libraries.
Please share your experience, and your You can give review\'s screenshort at 
our website or insta which you can find in my website Thank You.
___________________________________________________________________________________
How Was Your Experience? => """)
    print("\n")
    advice = input("""If there is any mistake in the bot or any advice you want to give,
please let us know.
Your feedback is valuable to us.
___________________________________________________________________________________
Is there any Mistake in Bot or any advice you want to give => """)
    print("\n")
def remove_special_characters(input_string): 
    special_characters =["~","`","!","@","#","$","%","^","&","*","(",")","_","-","=","+",
                        "{","}","[","]",":",";","\"","'","|","\\","<",">",",",".","?","/",]
    cleaned_string = ''
    for char in input_string:
        if char not in special_characters:
            cleaned_string += char
    return cleaned_string
def Youtube_Link():
    Yt_url = "https://www.youtube.com"
    webbrowser.open(Yt_url)
def Chat_Gpt_Link():
    GPT_url= "https://chat.openai.com/"
    webbrowser.open(GPT_url)
def Owner_Website():
    My_url = "https://mr-ferro.blogspot.com/"
    webbrowser.open(My_url)
def Source_Code_Link():
    Code_url = "https://mr-ferro.blogspot.com/2023/11/my-vpx-ai-code.html"
    webbrowser.open(Code_url)

#Bot Things😁 {Ignore I will Manage Later}

Ferro_Sound()
check_speaker_connection()
if speaker_connected == True:
    print("===="*30)
    Volume_And_Speech()
    print("===="*30)
Text_To_Speech_Lib = pyttsx3.init()
voices = Text_To_Speech_Lib.getProperty('voices')
indian_female_voice_index = 1
Text_To_Speech_Lib.setProperty('voice', voices[indian_female_voice_index].id)
Text_To_Speech_Lib.setProperty('volume', volume)
Text_To_Speech_Lib.setProperty('rate', speech_rate)

#Main Variables (+) Ferro Entry
Ferro_Banner()
YOU = "|~|--You--|~| =====> "
BOT = "|~| Ferro |~| =====> "
print("_______ Hi There , Ferro Here ________\n")

#Main Code {Looping}

while True:

#Input and then set All Text Data In Small Case

    user_input = input(YOU)
    user_input = user_input.lower().strip()
    user_input = remove_special_characters(user_input)

#Main Text Foam Reply To Text

    if user_input in BOT_Input.Hi_Message:
        response = random.choice(BOT_Output.Hi_Response)
        print(BOT , response)
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Fine_Message:
        response = random.choice(BOT_Output.Fine_Response)
        print(BOT , response)
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Bye_Message:
        response = random.choice(BOT_Output.Bye_Response)
        print(BOT , response)
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
        break
    elif user_input in BOT_Input.Thanks_Message:
        response = random.choice(BOT_Output.Thanks_Response)
        print(BOT , response)
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Blank_Message:
        response = random.choice(BOT_Output.Blank_Response)
        print(BOT , response)
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Owner_Details:
        response = random.choice(BOT_Output.Owner_Response)
        print(BOT , response)
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)

#Links Open

    elif user_input in BOT_Input.Open_YT:
        response = "Opening YouTube wait..."
        print(BOT , response)
        Youtube_Link()
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Chat_Gpt_Link:
        response = "Opening ChatGPT wait..."
        print(BOT , response)
        Chat_Gpt_Link()
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Open_My_url:
        response = "Opening My Website please wait..."
        print(BOT , response)
        Owner_Website()
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Open_Source_Code_Link:
        response = "Opening Please Wait..."
        print(BOT , response)
        Source_Code_Link()
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)

#Error Message if No Data Found

    else:
        response = random.choice(BOT_Input.No_Answer_Found)
        print(BOT , response)
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)

#Out and all command end 
Ferro_Banner()
print("_______ Bye There , Ferro Is Where? ________\n")
print("")
BOT_EXIT_Review()