#Librarys {Self}

import BOT_Input , Animations , Corrected_Words , BOT_Output , Links , banner , Const_Vari , Text_To_Speech , Check_Speaker

#Librarys {Public}

import random , subprocess , sys

#All Functions

def Next_line():
    Animations.Animation_Of_UnderScore_Slow()

#Main Variables (+) Ferro Entry

banner.Ferro_Banner()
print("_______ Hi There , Ferro Here ________\n")

#Main Code {Looping}

while True:

#Input and then set All Text Data In Small Case

    user_input = input(Const_Vari.YOU)
    user_input = user_input.lower().strip()
    user_input = Corrected_Words.Remove_Char_Not_Req(user_input)

#Main Text Foam Reply To Text

    if user_input in BOT_Input.Hi_Message:
        response = random.choice(BOT_Output.Hi_Response)
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
    elif user_input in BOT_Input.Fine_Message:
        response = random.choice(BOT_Output.Fine_Response)
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
    elif user_input in BOT_Input.Bye_Message:
        response = random.choice(BOT_Output.Bye_Response)
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
        break
    elif user_input in BOT_Input.Thanks_Message:
        response = random.choice(BOT_Output.Thanks_Response)
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
    elif user_input in BOT_Input.Blank_Message:
        response = random.choice(BOT_Output.Blank_Response)
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
    elif user_input in BOT_Input.Owner_Details:
        response = random.choice(BOT_Output.Owner_Response)
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()

#Links Open

    elif user_input in BOT_Input.Open_YT:
        response = "Opening YouTube wait..."
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
        Links.Youtube_Link()
    elif user_input in BOT_Input.Chat_Gpt_Link:
        response = "Opening ChatGPT wait..."
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
        Links.Chat_Gpt_Link()
    elif user_input in BOT_Input.Open_My_url:
        response = "Opening My Website please wait..."
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
        Links.Owner_Website()
    elif user_input in BOT_Input.Open_Source_Code_Link:
        response = "Opening Please Wait..."
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()
        Links.Source_Code_Link()

#Error Message if No Data Found

    else:
        response = random.choice(BOT_Input.No_Answer_Found)
        print(Const_Vari.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Next_line()

#Out and all command end 
banner.Ferro_Banner()
print("_______ Bye There , Ferro Is Where? ________\n")
print(" ")

Next_File_3 = 'Exit_Review.py'
subprocess.run(['python', Next_File_3])
sys.exit()
