"""
Script for moving cursor automatically to keep the display always on.
Last modified date: 2024/04/17
"""
import time
import random
import pyautogui
import keyboard


def setup_hint():
    pyautogui.alert(text='Step1: Move cursor to fix the location\n'
                         'Step2: Press ENTER key to continue.\n'
                         '## Click "Next" to get started with action!',
                    title='Hint!', 
                    button='Next')


def start_hint(_x, _y):
    pyautogui.alert(text=f'"Ctrl + C" to stop the script.\nX = {_x}, Y = {_y}\n# Click "Start" to get started!',
                    title='Hint!', 
                    button='Start')


def end_hint(count):
    pyautogui.alert(text=f'Stop the script!!\nTotal times: {count}',
                    title='Message', 
                    button='OK')      


def cursor_position():
    if keyboard.read_key() == "enter":
        _x, _y = pyautogui.position()
        print(f"Located at (x = {_x}, y = {_y})")
        return _x, _y


def mouse_event(_x, _y):
    bias_x = random.randint(50, 300)
    bias_y = random.randint(50, 300)
    localtime = time.localtime()
    currentime = time.strftime("%H:%M:%S", localtime)
    print(f'{currentime} move once')
    pyautogui.moveTo(_x + bias_x, _y + bias_y, duration=0.15)
    time.sleep(.5)
    pyautogui.moveTo(_x, _y, duration=0.15)
    time.sleep(.5)
    pyautogui.scroll(100)
    time.sleep(.5)
    pyautogui.scroll(-150)


if __name__ == "__main__":
    try:
        setup_hint()
        x, y = cursor_position()
        time.sleep(.5)
        start_hint(x, y)
        total_times = 0
        while True:
            if not keyboard.is_pressed('enter'):
                mouse_event(x, y)
                total_times += 1
                time.sleep(60)  # Move once per minute
            else:
                break
    finally:
        end_hint(total_times)

