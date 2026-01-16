import pyautogui
import time

time.sleep(3)
# x1, y1, x2, y2
x1, y1, x2, y2 = 1864, 0, 1919, 39

# Convert to pyautogui region
region = (x1, y1, x2 - x1, y2 - y1)

img = pyautogui.screenshot(region=region)
img = img.convert("L")
img.save("button3.png")
print("captured")