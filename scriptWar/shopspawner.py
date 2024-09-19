import time
import keyboard
import pyautogui

def open_shop():
  pyautogui.press('t')
  for c in "/spawnershop":
    pyautogui.press(c)
  pyautogui.press('enter')

def move_and_buy():
  x, y = 923, 451
  pyautogui.moveTo(x, y)
  pyautogui.click()

while True:
  if keyboard.is_pressed('esc'):
    break
  if keyboard.is_pressed('p') or True:
    time.sleep(0.1)
    open_shop()
    time.sleep(0.1)   
    move_and_buy()
