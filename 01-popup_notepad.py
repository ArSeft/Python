import time
import pyautogui
import subprocess

def auto_type(phrase, delay=0.01):
    for character in phrase:
        pyautogui.typewrite(character)
        time.sleep(delay)

def open_notepad():
    subprocess.Popen(['notepad.exe'])

if __name__ == "__main__":
    user_phrase = "I see you."
    
    open_notepad()

    time.sleep(1)

    auto_type(user_phrase)