import pyautogui
import time
import keyboard
time.sleep(2)
def simulate_typing(text):
    words = text.split()
    for word in words:
        print(word)
        pyautogui.typewrite(word)
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(1)

# Read the text file
file_path = "bee.txt"
with open(file_path, "r") as file:
    text_content = file.read()

# Simulate typing
simulate_typing(text_content)
