"""Update:2023/04/04"""
import time
import random
import pyautogui
import keyboard


def setup_hint():
    pyautogui.alert(text='Please press ENTER after moving to the click location.', 
                    title='Hint!', 
                    button='Next')

def start_hint(x, y):
    pyautogui.alert(text=f'Press SPACE to end.\nX = {x}, Y = {y}', 
                    title='Hint!', 
                    button='Start')

def end_hint(count):
    pyautogui.alert(text=f'End of script\nTotal click: {count} times.', 
                    title='Message', 
                    button='OK')      

def cursor_position():
    if keyboard.read_key() == "enter":
        x, y = pyautogui.position()
        print(f"x = {x}, y = {y}")
        return x, y

def click_event(x, y):
    delay_time = random.randint(1, 3) / 10
    bias_x = random.randint(1, 50)
    bias_y = random.randint(1, 50)
    pyautogui.click(x + bias_x, y + bias_y)
    time.sleep(delay_time)



if __name__ == "__main__":
    setup_hint()
    x, y = cursor_position()
    time.sleep(.5)
    start_hint(x, y)
    count = 0
    while True:
        if not keyboard.is_pressed('enter'):
            click_event(x, y)
            count+=1
        else:
            break
    end_hint(count)

