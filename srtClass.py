#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pysubs2
# srt文件处理类
class SrtClass(object):
    def __init__(self,path):
        # 文件路径
        self.path=path
        self.loadSrt()

        return

    # 载入srt字符串
    def loadSrt(self):
        self.strArr = pysubs2.load(self.path, encoding="utf-8")
        self.processStr()

    # 处理字符串的空白
    def processStr(self):
        for i in range(len(self.strArr)):
            self.strArr[i].text=self.strArr[i].text.strip()