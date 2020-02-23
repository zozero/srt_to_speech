# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from baiduApiClass import BaiduApi

if __name__ == '__main__':
    # 启动合成类
    synt = BaiduApi()
    # 第二个参数为发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
    synt.synthesis('量子力学试图解释亚原子粒子的行为',0)

    del synt