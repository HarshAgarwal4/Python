import pyautogui
import time
import os
import webbrowser
from utils.common import resource_path

pyautogui.FAILSAFE = True
# time.sleep(3)

def closeWindow():
    closing_Images = [
        resource_path(os.path.join("pyAutoGUI_mouse" , "images\\button1.png")),
        resource_path(os.path.join("pyAutoGUI_mouse" , "images\\button2.png")),
        resource_path(os.path.join("pyAutoGUI_mouse" , "images\\button3.png")),
    ]
    time.sleep(2)
    try:    
        for i in closing_Images:
            try:
                pos = pyautogui.locateCenterOnScreen(
                    i,
                    confidence=0.75
                )
                if pos:
                    print(pos.x , pos.y)
                    pyautogui.click(pos)
            except Exception as e:
                 print(e)
    except Exception as e:
        print(e)
        print("Button not found on screen")

def switchTab():
    pyautogui.hotkey('alt' , 'tab')

def showTabs():
    pyautogui.hotkey('super' , 'tab')

def open(text):
    pyautogui.press('super')
    time.sleep(1)
    pyautogui.write(text , 0.1)
    time.sleep(1)
    pyautogui.press('enter')

cursor_properties = {
    'very-little': 10,
    'little' : 25,
    'medium' : 50,
    'large' : 100,
    'very large' : 200
}

def move_cursor(q , direction):
    size_x,size_y = pyautogui.size()
    x,y = pyautogui.position()
    fc_x=fc_y=0
    amt = cursor_properties.get(q)
    if q.isdigit():
        fc_x = (int(q)/100)*size_x 
        fc_y = (int(q)/100)*size_y 
    if amt:
        fc_x = fc_y = amt
    if direction == 'up' :
            y = y - fc_y
    if direction == 'down' : 
            y=y+fc_y
    if direction == 'left' : 
            x= x-fc_x
    if direction == 'right' : 
            x = x+fc_x
    if direction == 'top right' or direction == 'top-right': 
            x=x+fc_x
            y=y-fc_y
    if direction == 'top left' or direction == 'top-left':
            y=y-fc_y
            x=x-fc_x
    if direction == 'bottom right' or direction == 'bottom-right':
            x=x+fc_x
            y=y+fc_y
    if direction == 'bottom left' or direction == 'bottom-left':
            x=x-fc_x
            y=y+fc_y
    pyautogui.moveTo(x,y, 0.5)

def click() :
    pyautogui.click()

def write(text) :
    pyautogui.write(text)

def screenshot():
    img = pyautogui.screenshot()
    img.show()

if __name__ == "__main__":
    screenshot()
    # switchTab()
    # showTabs()
    # open('14_JARVIS')
    # time.sleep(1)
    # move_cursor('50' , 'top-right')