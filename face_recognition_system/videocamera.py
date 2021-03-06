""" This module contains the class VideoCamera, this classs provides us with
automtic functions to turn on the camera, record and turn off the camera
in the correct way.
"""

import cv2
import os

class VideoCamera(object):
    """ A class to handle the video stream.
    """
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(3,320)
        self.video.set(4,240)

    def __del__(self):
        self.video.release()

    def get_frame(self, in_grayscale=False):
        """ Get current frame of a live video.
        """
        success , frame = self.video.read()

        if in_grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        return frame

    def show_frame(self, seconds, in_grayscale=False):
        """ Show the frame of the live video.

        This function will show the current frame of the live video during
        the specified seconds. The frame is displayed in an external window.
        It also captures the key pressed during the time the frame was shown.
        This key can be used as an action indicator from the user.
        """
        _, frame = self.video.read()
        if in_grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('SnapShot', frame)
        key_pressed = cv2.waitKey(seconds * 1000)

        return key_pressed & 0xFF

if __name__ == '__main__':
    VC = VideoCamera()
    while True:
        KEY = VC.show_frame(1, True)
        if KEY == 27:
            break
    VC.show_frame(1)

