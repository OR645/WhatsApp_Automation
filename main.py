import webbrowser
import pyautogui
from auto import WhatsApp
from time import sleep


webbrowser.open('https://wa.me/972555649522')

bot = WhatsApp(speed=.3, click_speed=.1)

sleep(1)

bot.open_whatsapp()
bot.nav_paperclip()
pyautogui.typewrite('You got hired! \n')

sleep(3)

pyautogui.hotkey('alt', 'fn', 'f4')
