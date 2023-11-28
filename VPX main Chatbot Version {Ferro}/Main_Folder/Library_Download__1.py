#Librarys {Self}

import banner , Const_Vari

#Librarys {Public}

import subprocess , sys


def install_or_update_libraries():
    libraries = ["pyautogui"]
    for library in libraries:
        print(f"{Const_Vari.Space_Big}{Const_Vari.System_Message}Installing And updating {library}...{Const_Vari.Space_Big}")
        subprocess.run(f"pip install --upgrade {library}", shell=True)

banner.Ferro_Updating_Banner()
install_or_update_libraries()

Next_File_1 = 'Library_Download__2.py'
subprocess.run(['python', Next_File_1])
sys.exit()