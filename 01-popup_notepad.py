import time
import pyautogui
import subprocess

def auto_type(phrase, delay=0.01):
    """
    Automatically types a given phrase character by character with a delay between each.

    Parameters:
    phrase (str): The string to type out.
    delay (float): Time to wait (in seconds) between typing each character. Default is 0.01 seconds.

    Behavior:
    Uses pyautogui to simulate keyboard input, typing each character of the provided phrase
    sequentially with a short pause, to mimic natural typing.
    """
    for character in phrase:
        pyautogui.typewrite(character)
        time.sleep(delay)

def open_notepad():
    """
    Opens the Windows Notepad application.

    Behavior:
    Uses subprocess to launch 'notepad.exe'. Assumes the script is running on a Windows system
    where Notepad is available in the system PATH.
    """
    subprocess.Popen(['notepad.exe'])

if __name__ == "__main__":
    """
    Main execution block of the script.

    Behavior:
    1. Defines a user phrase to type ("I see you.").
    2. Opens Notepad using the open_notepad() function.
    3. Waits briefly (1 second) to allow Notepad to load.
    4. Simulates typing the defined phrase into the open Notepad window using auto_type().
    """
    user_phrase = "I see you."
    
    open_notepad()

    time.sleep(1)

    auto_type(user_phrase)
