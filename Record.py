import cv2
from imutils import resize
from _datetime import datetime as dt


class Record:

    error = False

    def __init__(self, width, height, i):
        name = str(dt.now().strftime("%d.%m.%Y_%H:%M:%S"))

        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        self.width = width
        self.out = cv2.VideoWriter('output {}.avi'.format(name), fourcc, 20.0, (width, height), True)

    def record_video(self, frame):
        if self.out is not None:
            frame = resize(frame, width=self.width)
            self.out.write(frame)
        else:
            self.error = True
            print("[Error] VideoWriter not initialized!")
            self.__del__()

    def __del__(self):
        self.out.release()