import webbrowser
import pyautogui
from auto import WhatsApp
from time import sleep


webbrowser.open('https://wa.me/972555649522', new=2)

bot = WhatsApp(speed=.3, click_speed=.4)

sleep(2)

if bot.open_whatsapp():
    bot.nav_paperclip()
    sleep(2)
    pyautogui.typewrite('You got hired! \n')
    sleep(3)
    pyautogui.hotkey('alt', 'fn', 'f4')
else:
    pass

