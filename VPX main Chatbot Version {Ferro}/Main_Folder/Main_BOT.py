#Librarys {Self}

import BOT_Input , BOT_Output , Links

#Librarys {Taken}

import random , pyttsx3 ,  sys , time , pyaudio

#All Functions

def Animation_Of_Tilt():
    for _ in range(139):
        sys.stdout.write("~")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_Tilt_Slow():
    for _ in range(139):
        sys.stdout.write("~")
        sys.stdout.flush()
        time.sleep(0.01)
def Animation_Of_UnderScore():
    for _ in range(139):
        sys.stdout.write("_")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_UnderScore_Slow():
    for _ in range(139):
        sys.stdout.write("_")
        sys.stdout.flush()
        time.sleep(0.01)
def Animation_Of_Straight_Line():
    for _ in range(139):
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_Straight_Line_Slow():
    for _ in range(139):
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.01)
def Animation_Of_Slash():
    for _ in range(139):
        sys.stdout.write("/")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_Slash_Slow():
    for _ in range(139):
        sys.stdout.write("/")
        sys.stdout.flush()
        time.sleep(0.01)
def Animation_Of_BackSlash():
    for _ in range(139):
        sys.stdout.write("\\")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_BackSlash_Slow():
    for _ in range(139):
        sys.stdout.write("\\")
        sys.stdout.flush()
        time.sleep(0.01)
def Animation_Ferro_Banner():
    Animation_Of_Straight_Line()
    Animation_Of_Straight_Line()
def Animation_Ferro_Sound_Banner():
    Animation_Of_Straight_Line()
    Animation_Of_BackSlash()
    Animation_Of_Slash()
    Animation_Of_Straight_Line()
def speak(text):
    Text_To_Speech_Lib.say(text)
    Text_To_Speech_Lib.runAndWait()
def Remove_Char_Not_Req(input_string):
    special_characters =["~","`","!","@","#","$","%","^","&","*","(",")","_","-","=","+",
                        "{","}","[","]",":",";","\"","'","|","\\","<",">",",",".","?","/",]
    cleaned_string = ''
    for char in input_string:
        if char not in special_characters:
            cleaned_string += char
    return cleaned_string
def BOT_EXIT_Review():
    EXP = input("""This Bot is Made By Vikrant Pathania, a School Student of 16 years.
He made this using 100% Python, random, and webbrowser libraries.
Please share your experience, and your You can give review\'s screenshort at 
our website or instagram which you can find in my website Thank You.
___________________________________________________________________________________
How Was Your Experience? => """)
    print("\n")
    advice = input("""If there is any mistake in the bot or any advice you want to give,
please let us know.
Your feedback is valuable to us.
___________________________________________________________________________________
Is there any Mistake in Bot or any advice you want to give => """)
    print("\n")
def check_speaker_connection():
    global num_devices, speaker_connected, volume , speech_rate
    speaker_connected = False
    p = pyaudio.PyAudio()
    try:
        num_devices = p.get_device_count()
        if num_devices > 0:
            Animation_Of_Tilt_Slow()
            print("Speakers are connected to your computer.")
            Animation_Of_UnderScore_Slow()
            print("Checking all other devices connected to your computer:")
            Animation_Of_UnderScore_Slow()
            speaker_connected = True
            for i in range(num_devices):
                device_info = p.get_device_info_by_index(i)
                Animation_Of_UnderScore_Slow()
                if device_info['maxOutputChannels'] > 0:
                    print(f"Device {i}: {device_info['name']}")
        else:
            Animation_Of_Tilt_Slow()
            print("No speaker is Not connected. Volume is set to 0.")
            Animation_Of_Tilt_Slow()
            speaker_connected = False
    except Exception as e:
        print(f"An error occurred: {e}")
        speaker_connected = False
        volume=0
        speech_rate = 0
def Ferro_Sound_Banner():
    Animation_Ferro_Sound_Banner()
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
    Animation_Ferro_Sound_Banner()   
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

#Variables 

Space = " "
Volume_Applied = None
volume = None
speech_rate = None

#Bot Things😁 {Ignore I will Manage Later}

Ferro_Sound_Banner()
print(Space)
print(Space)
check_speaker_connection()
print(Space)
print(Space)
Animation_Of_Tilt_Slow()
print(Space)
print(Space)
if speaker_connected == True:   
    print("""  ~~~~  Please Type  ~~~~
    \'H\'or\'High\' = For High Level Of Sound + Speech Rate
    \'L\'or\'Low\' = For Low Level Of Sound + Speech Rate
    \'D\'or\'Default\' = For Default Level Of Sound + Speech Rate
    \'N\'or\'None\' = For No Sound + Speech Rate
    *Note If You Type AnyThing Wrong Then It will Set Sound To Default
    #You can Ignore The UpperCase Or Lower Case""")
    print(Space)
    print(Space)
    Sound_Level = str(input("Please Tell What Level Of Sound You Want ===>")).lower()
    print(Space)
    print(Space)
    if Sound_Level == "h" or "high":
        print("Volume Set To High")
        volume = 100
        speech_rate = 150
        Volume_Applied = True
    elif Sound_Level == "l" or "low":
        print("Volume Set To Low")
        volume = 50
        speech_rate = 150
        Volume_Applied = True
    elif Sound_Level == "d" or "default":
        print("Volume Set To Default")
        volume = 75
        speech_rate = 150
        Volume_Applied = True
    elif Sound_Level == "n" or "none":
        print("Volume Set To None")
        volume = 0
        speech_rate = 0
        Volume_Applied = False
    else:
        print("There Is an Error In Your Input. Volume = Default")
        volume = 75
        speech_rate = 150
        Volume_Applied = True
else:
    print("No Speaker Connected To Your device Now We Will Go Further")
    volume = 0
    speech_rate = 0
    Volume_Applied = False
Animation_Of_Tilt_Slow()

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
    user_input = Remove_Char_Not_Req(user_input)

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
        Links.Youtube_Link()
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Chat_Gpt_Link:
        response = "Opening ChatGPT wait..."
        print(BOT , response)
        Links.Chat_Gpt_Link()
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Open_My_url:
        response = "Opening My Website please wait..."
        print(BOT , response)
        Links.Owner_Website()
        if speaker_connected == True:
            if Volume_Applied == True:
                speak(response)
    elif user_input in BOT_Input.Open_Source_Code_Link:
        response = "Opening Please Wait..."
        print(BOT , response)
        Links.Source_Code_Link()
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
