import cv2 as cv
import pyautogui
import Window_capture
import mss
import numpy as np
import PIL


class Main():
    def __init__(self, ):
        self.sct = mss.mss()
        super(Main, self).__init__()

    def run(self):
        while True:
            image = PIL.ImageGrab.grab(bbox=(
                0,
                390,
                440,
                50,
            ))
            image.show()


if __name__ == '__main__':
    main = Main()
    main.run()
