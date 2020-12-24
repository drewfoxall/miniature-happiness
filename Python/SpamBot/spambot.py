import pyautogui
import time
time.sleep(5)
f = open("SpamBot\Beemovie.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")