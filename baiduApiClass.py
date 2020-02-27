#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 百度api返回的数据是mp3格式，需要加载额外的程序才可处理
import configparser
from baidu_API.aip import AipSpeech

class BaiduApi(object):
    def __init__(self):
        msg = self.__setApiInfo()
        if (msg != 0):
            print(msg)

        self.__client = AipSpeech(self.__appId, self.__apiKey, self.__secretKey)

    # text 需要合成的文本
    # per 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女 度博文=106，度小童=110，度小萌=111，度米朵=103，度小娇=5
    def synthesis(self, text, per=0):
        return self.__client.synthesis(text, 'zh', 1, {
            'per': per,
            'aue': 6,
        })

    # 设置api信息
    def __setApiInfo(self):
        msg = 0
        # 读取配置文件
        config = configparser.ConfigParser()
        if len(config.read("./env.ini")) == 0:
            msg = '没有配置文件'
        else:
            # 以下信息需要百度智能云生成应用时获得
            if 'Baidu_API' in config:
                if ('APP_ID' in config['Baidu_API']):
                    self.__appId = config['Baidu_API']['APP_ID'].strip()
                    if (self.__appId == ''):
                        msg = 'APP_ID字段是空的'
                    else:
                        msg = 0
                else:
                    msg = 'APP_ID字段不存在'

                if ('API_KEY' in config['Baidu_API']):
                    self.__apiKey = config['Baidu_API']['API_KEY'].strip()
                    if (self.__apiKey == ''):
                        msg = 'API_KEY字段是空的'
                    else:
                        msg = 0
                else:
                    msg = 'API_KEY字段不存在'

                if ('SECRET_KEY' in config['Baidu_API']):
                    self.__secretKey = config['Baidu_API']['SECRET_KEY'].strip()
                    if (self.__secretKey == ''):
                        msg = 'SECRET_KEY字段是空的'
                    else:
                        msg = 0
                else:
                    msg = 'SECRET_KEY字段不存在'
            else:
                msg = '请按照要求配置好env.ini文件'
        return msg

    def __del__(self):
        print('百度语音合成类使命完成')
