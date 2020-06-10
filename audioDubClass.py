#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pydub import AudioSegment, effects
import time


# 封装音频处理类
class AudioDub(object):
    def __init__(self):

        return

    # 添加空白
    # sound 音频
    # time  留空的时间
    def addLacuna(self, time):
        return AudioSegment.silent(duration=time)

    # 返回一个空的pydub对象
    def getEmpty(self):
        return AudioSegment.empty()

    # 获得一段音频
    def getSound(self, stream):
        return AudioSegment(
            # raw audio data (bytes) 二进制数据流
            data=stream,
            #  采样位数 2 byte (16 bit) samples 通常有8bit、16bit、24bit和32bit等几种
            sample_width=2,

            # 44.1 kHz frame rate 采样率
            frame_rate=16000,

            # 声道 stereo 1 单声道
            channels=1
        )

    # 音频合并
    # frontSound 放在前面的音频
    # behindSound   放在后面的音频
    def mergeSound(self, frontSound, behindSound):
        # 为过渡的时间添加空白
        frontSound += AudioSegment.silent(duration=100)
        # crossfade 用于过渡的时间
        return frontSound.append(behindSound, crossfade=100)

    # 导出音频
    def exportAudio(self, sound, name='test.wav'):
        formtTime = time.strftime("%Y-%m-%d", time.localtime())
        sound.export('./sound/' + formtTime + '_' + name, format="wav")

    # 语音加速
    def speedSound(self, sound, keepTime):
        # 上一个的长度
        beforeLen = 0
        left = 100
        right = 130
        beforeSound = 0
        curSound = 0
        toalCount = 0
        while left < right:
            toalCount = toalCount + 1
            middle = int((left + right) / 2)
            # 参数： 音频 倍数 块大小 过渡时间
            curSound = effects.speedup(sound, middle / 100, 300, 100)
            soundLen = len(curSound)
            if soundLen == keepTime:
                return curSound
            elif right - left == 1 and soundLen < keepTime and soundLen < beforeLen:
                return beforeSound
            elif soundLen < keepTime:
                right = middle + 1
                beforeSound = curSound
                beforeLen = soundLen
            elif soundLen > keepTime:
                left = middle + 1
                beforeSound = curSound
                beforeLen = soundLen
            if toalCount == 30:
                break
        return curSound
