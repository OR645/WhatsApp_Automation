import pyautogui


class WhatsApp:
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    def open_whatsapp(self):

        try:
            position = pyautogui.locateOnScreen('assets/open_whatsapp.png', confidence=.9)
            pyautogui.moveTo(position[0:2], duration=self.speed)
            pyautogui.moveRel(15, 30, duration=self.speed)
            pyautogui.doubleClick(interval=self.click_speed)
            return True

        except Exception as error:
            print(f'open_whatsapp {error}')

    def nav_paperclip(self):

        try:
            position = pyautogui.locateOnScreen('assets/paperclip.png', confidence=.7)
            pyautogui.moveTo(position[0:2], duration=self.speed)
            pyautogui.moveRel(100, 10, duration=self.speed)
            pyautogui.doubleClick(interval=self.click_speed)

        except Exception as error:
            print(f'nav_paperclip {error}')
