#pip install pyautogui
import pyautogui
import keyboard


def type_erfan_10_times():
    for _ in range(100):
        pyautogui.typewrite("@eerfan")
        pyautogui.press('enter')  
        pyautogui.press('enter')


activate_key = 'space' 


keyboard.wait(activate_key)


type_erfan_10_times()
