import subprocess
import sys
import time

System_Message = "| ~ | System | ~ | =========> "
Space = """


"""
Arrow = "==>"
repeat = 1
star_difference = 1
lines =75
Time = 0.03
def Animation_Ferro_Banner():
    for _ in range(278):
        sys.stdout.write("~")
        sys.stdout.flush()
        time.sleep(0.001)
def Ferro_Updating_Banner():
    Animation_Ferro_Banner()
    print("""
                                        ██    ██ ██████  ██████   █████  ████████ ██ ███    ██  ██████  
                                        ██    ██ ██   ██ ██   ██ ██   ██    ██    ██ ████   ██ ██       
                                        ██    ██ ██████  ██   ██ ███████    ██    ██ ██ ██  ██ ██   ███ 
                                        ██    ██ ██      ██   ██ ██   ██    ██    ██ ██  ██ ██ ██    ██ 
                                         ██████  ██      ██████  ██   ██    ██    ██ ██   ████  ██████                                                                                                                                                 
            """)
    Animation_Ferro_Banner()
def install_or_update_libraries():
    libraries = ["pyautogui"]
    for library in libraries:
        print(f"{Space}{System_Message}Installing And updating {library}...{Space}")
        subprocess.run(f"pip install --upgrade {library}", shell=True)

Ferro_Updating_Banner()
install_or_update_libraries()
file_two_path = 'Library_Download__2.py'
subprocess.run(['python', file_two_path])
sys.exit()