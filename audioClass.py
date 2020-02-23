#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pydub import AudioSegment

class BaiduApi(object):
    def __init__(self):
        return

    # 音频处理
    def manipulateAudio(self):
        sound = AudioSegment(
            # raw audio data (bytes)
            # data=b'…',

            # 2 byte (16 bit) samples
            sample_width=2,

            # 44.1 kHz frame rate
            frame_rate=44100,

            # stereo
            channels=2
        )
        return