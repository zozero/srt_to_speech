# !/usr/bin/python3
# -*- coding: UTF-8 -*-

from tencentApiClass import TencentApi
# 百度的尚未完成
# from baiduApiClass import BaiduApi
from srtClass import SrtClass
from audioDubClass import AudioDub
def init():
    # 启动合成类
    synt = TencentApi()
    # 启动生成音频类
    dub = AudioDub()
    # 获得pydub空对象
    sound = dub.getEmpty()

    # 处理srt文件
    srt = SrtClass("./srt/test.srt")
    # 获得第一段前的空白时间
    time = srt.strArr[0].start - 0
    # 拿出最后一个，它们需要特殊处理
    sArr = srt.strArr[:-1]
    # 计数
    count = 1
    # 循环生成音频
    for i in range(len(sArr)):
        print(i + 1)
        # 生成空白的时间
        sound += dub.addLacuna(time)
        # 当前音频持续时间
        time = srt.strArr[i].end - srt.strArr[i].start
        # 获得音频流
        stream = synt.getStream(text=srt.strArr[i].text, keepTime=time)
        # 用于计算差值，添加空白
        tmpSound = dub.getSound(stream)
        # 查看两者时间值
        tmpTime = time - len(tmpSound)
        print(tmpTime)
        if(tmpTime < -300):
            # 裁剪将会少字，建议将十分长的话在srt文件中缩短
            # 重新修剪
            tmpSound = dub.speedSound(tmpSound, time)
        # 合并音频，因为之前的声音都是空白所有可以直接加
        sound = dub.mergeSound(sound, tmpSound)

        print('srt文件时间：' + str(time))
        print('音频时间：' + str(len(tmpSound)))
        print('留白时间：' + str(time - len(tmpSound)))

        # 再次查看两者时间值
        tmpTime = time - len(tmpSound)
        # 可能出现最快速度也大于srt的时间，那么直接裁剪
        if (tmpTime < 0):
            sound = sound[:tmpTime]
        else:
            # 添加空白
            sound += dub.addLacuna(tmpTime)
        # 设置第一段与第二段之间的空白
        time = srt.strArr[i + 1].start - srt.strArr[i].end
        print('分段时间：' + str(time))
        # 命名
        name = str(count) + '.wav'
        count = count + 1
        # 限制生成文件的数量
        if count > 3:
            count = 1
        # 防报错导出部分音频
        dub.exportAudio(sound, name)

    # # 获得音频流
    stream = synt.synthesis(text=srt.strArr[-1].text)
    # # 用于计算差值，添加空白
    sound = dub.mergeSound(sound, dub.getSound(stream))
    print('声音导出完毕!')
    # 导出音频
    dub.exportAudio(sound)

if __name__ == '__main__':
    # 开始行动
    init()
