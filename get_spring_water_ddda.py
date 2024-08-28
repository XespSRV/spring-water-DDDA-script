import pyautogui
import time

# delay to start the script
time.sleep(10) 

def press_action_key(x):

  for _ in range(x):
    pyautogui.press('e')
    time.sleep(1.5)

# number of time that the action key will be pressed
x = 40 

press_action_key(x)