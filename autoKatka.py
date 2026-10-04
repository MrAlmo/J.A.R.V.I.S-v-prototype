import pyautogui
import keyboard
import threading
import time

stop_flag = True

def stop_f():
    global stop_flag
    keyboard.wait('right shift')
    stop_flag = False

def find_press():
    try:
        location = pyautogui.locateOnScreen("media/button.png", confidence=0.8)

        if location:
            print(f"Picture located at {location}")
            pyautogui.press('enter')
        else:
            print(f"Picture not found")
    except Exception as ex:
        print("Error occured", ex)

if __name__ == "__main__":
    threading.Thread(target=stop_f).start()

    while stop_flag:
        time.sleep(3)
        find_press()

