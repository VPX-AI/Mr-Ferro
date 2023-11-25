speaker_connected = True

if speaker_connected:
    volume = int(input("Please Enter The Volume You Want to Add ===> "))

    if 0 < volume <= 100:
        print(f"Volume Is Applied To ===> {volume}")
        Volume_Applied = True
    elif not (0 < volume <= 100):
        print(f"""Hey User, You Have Applied Volume To {volume}
This Amount Of Volume Is Not Valid, So I Set the Default Volume to '100'""")