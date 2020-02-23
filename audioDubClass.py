#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pydub import AudioSegment
from pydub.playback import play


class AudioDub(object):
    def __init__(self, stream):
        self.__stream = stream
        print(self.__stream)
        # self.awesome = self.manipulateAudio()
        # self.exportAudio()
        return

    # 音频处理
    def manipulateAudio(self):
        sound = AudioSegment.from_file(self.__stream, format="wav")
        play(sound)
        print(1)
        # return AudioSegment.from_wav(self.__stream)

    def exportAudio(self):
        # self.awesome.export("audiodub.wav", format="wav")
        return