#!/usr/bin/env python3

import pyautogui
import keyboard
import re
import time

filename = "C:/Users/Peppe/AppData/Roaming/.minecraft/logs/latest.log"

def LastLine():
  pattern = r"Bilancio:.*€$"
  with open(filename) as f:
      last_line = ""
      for line in f:
          if re.search(pattern, line.strip()):
             last_line = line.strip()
      return last_line

def LastLineSell():
  pattern = r"Shop » Hai venduto tutto Gunpowder.*.$"
  with open(filename) as f:
      last_line = ""
      for line in f:
          if re.search(pattern, line.strip()):
             last_line = line.strip()
      return last_line.split()

def print_money():
  pyautogui.press('t')
  for c in "/money":
    pyautogui.press(c)
  pyautogui.press('enter')

def human_readable_money(newline):
   return newline.split()[-1]

def float_money(newline):
   return float(newline.split()[-1][:-1].replace(",", ""))

def get_current_money_data():
   print_money()
   time.sleep(1)
   new_line = LastLine()
   return human_readable_money(new_line), float_money(new_line)

def float_to_readable(n):
  n_to_string = f"{n:.2f}"
  firstpart, secondpart = n_to_string.split(".")
  firstpart = firstpart[::-1]
  output = ""
  for i in range(len(firstpart)):
    if i % 3 == 0:
      output = "," + output
    output = firstpart[i] + output 
  if output[-1] == ",":
     output = output[:-1]  
  return output + "." + secondpart + "€"

def get_money_earned():
  newline = LastLineSell()
  try:
    moneyget = float(newline[-1][1:-1].replace(",",""))
  except:
    moneyget = 0
  return moneyget

def continue_to_sell():
   if get_money_earned() >= 7000:
      return True
   return False

if __name__ == "__main__":   
  while True:
    if keyboard.is_pressed('p'):
      print(get_money_earned())
      print(continue_to_sell())
      break