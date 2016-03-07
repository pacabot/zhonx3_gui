from kivy.logger import Logger
import logging
from kivy.app import App

import serial

Logger.setLevel(logging.DEBUG)


class ZhonxGUIApp(App):
    def build(self):
        pass
        
    
        
if __name__ == '__main__':
    ZhonxGUIApp().run()
    