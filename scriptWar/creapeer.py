import time
import keyboard
import pyautogui
import readlogs

def open_shop():
  pyautogui.press('t')
  for c in "/shop":
    pyautogui.press(c)
  pyautogui.press('enter')

def move_to_drop():
  x, y = 960, 468
  pyautogui.moveTo(x, y)
  pyautogui.click()

def move_to_gunpowder_and_sell_it():
  x, y = 925, 415
  pyautogui.moveTo(x, y)
  with pyautogui.hold('shift'):
    #pyautogui.click(button='right', clicks=80, interval=0.6)
    #best clicks = 40/45
    flag = True
    i = 0
    while flag:
      pyautogui.click(button='right')
      time.sleep(0.7)#quando non c'e' nessuno nel server e non lagga va bene pure 0.6
      i += 1
      flag = readlogs.continue_to_sell()
    print("inv selled", i)

def sell():
  time.sleep(0.5)
  open_shop()
  time.sleep(0.5)
  move_to_drop()
  time.sleep(0.5)
  move_to_gunpowder_and_sell_it()
  time.sleep(0.5)
  pyautogui.press('esc')

def hit():
  time.sleep(0.6)
  pyautogui.click()

def print_total_data(start_time, F_money1, H_money1):
  tot_time = time.time() - start_time
  s = int(tot_time % 60)
  m = int(tot_time // 60)
  h = int(m // 60)
  display_time = f"{h:02d}:{m:02d}:{s:02d}"  
  time.sleep(5)
  H_money2, F_money2 = readlogs.get_current_money_data()
  earned_money = readlogs.float_to_readable(F_money2 - F_money1)
  for_minute = readlogs.float_to_readable((F_money2 - F_money1) / (tot_time / 60))
  for_hour = readlogs.float_to_readable((F_money2 - F_money1) / (tot_time / 60) * 60) 

  print("=" * 46)
  print(f"Start Money             : {H_money1:>20}")
  print(f"End Money               : {H_money2:>20}")
  print(f"Earned Money            : {earned_money:>20}")
  print(f"Earned Money for minute : {for_minute:>20}")
  print(f"Earned Money for hour   : {for_hour:>20}")
  print("=" * 46)
  print(f"Execution time          : {display_time:>20}")
  print("=" * 46)


last_time = None
on = False
while True:
  if keyboard.is_pressed('p'):
    start_time = time.time()
    H_money1, F_money1 = readlogs.get_current_money_data()
    on = True
    last_time = time.time()
  if keyboard.is_pressed('k'):
    break
  if on:
    hit()
  if last_time and time.time() - last_time >= 30:
    sell()
    last_time = time.time()
print_total_data(start_time, F_money1, H_money1)
