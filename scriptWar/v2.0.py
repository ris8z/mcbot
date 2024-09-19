from pywinauto import Application
import time

mcTitle = "Minecraft 1.20.1 - Multiplayer (3rd-party Server)"
app = Application(backend="win32").connect(title=mcTitle, class_name="GLFW30")

def sell_inv(n=1, t=1):
  for _ in range(n):
    app.window(title=mcTitle).send_keystrokes("t")
    time.sleep(0.1)
    app.window(title=mcTitle).send_keystrokes("{UP}{ENTER}")
    time.sleep(t)

def click():
  app.window(title=mcTitle).click(button='left')


start_time = last_time = time.time()
while True:
  click()
  time.sleep(1)
  if time.time() - last_time >= 20:
      sell_inv(40)
      last_time = time.time()
