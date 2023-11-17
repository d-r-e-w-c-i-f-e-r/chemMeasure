import cv2
import numpy as np


class Video:

    def __init__(self, path, capture_count=12):
        self.path = path
        self.cap = cv2.VideoCapture(path)
        self.frames = list()
        self.capture_count = capture_count
        if not self.cap.isOpened():
            print("Error opening video file.")
            exit()
        self.__frames()

    # Reads the frames from the video and stores them in the self.frames array.
    def __frames(self):
        count = 0
        while True:
            count += 1
            ret, frame = self.cap.read()
            if not ret:
                break
            if count % self.capture_count == 0:
                success, frame = cv2.imencode(".png", frame)
                if success:
                    print("frame", count, "grabbed")
                    self.frames.append(frame)

        self.cap.release()

    def get_frames(self):
        return self.frames

    def get_capture_count(self):
        return self.capture_count


