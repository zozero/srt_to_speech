#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import configparser
# 导入腾讯的pythonSDK GitHub：https://github.com/TencentCloud/tencentcloud-sdk-python
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tts.v20190823 import tts_client, models
import uuid
import base64
import json

class TencentApi(object):
    def __init__(self,text,voiceType='0'):
        msg = self.__setApiInfo()
        if (msg != 0):
            print(msg)
        self.__synthesis(text,voiceType)

    # 腾讯tts请求的参数设置
    # Text 需要转换成语音的文本
    # VoiceType 声音的类型 包括
    # 0-云小宁，亲和女声(默认)
    # 1-云小奇，亲和男声
    # 2-云小晚，成熟男声
    # 4-云小叶，温暖女声
    # 5-云小欣，情感女声
    # 6-云小龙，情感男声
    # 1000-智侠、情感男声（新）
    # 1001-智瑜，情感女声（新）
    # 1002-智聆，通用女声（新）
    # 1003-智美，客服女声（新）
    # 1050-WeJack，英文男声（新）
    # 1051-WeRose，英文女声（新）
    def __synthesis(self, text, voiceType='0'):
        try:
            # 获取腾讯云凭证
            cred = credential.Credential(self.__secretId, self.__secretKey)
            # 请求的配置
            httpProfile = HttpProfile()
            # 请求访问的域名
            httpProfile.endpoint = "tts.tencentcloudapi.com"
            # sdk的配置
            clientProfile = ClientProfile()
            # 设置sdk的请求配置
            clientProfile.httpProfile = httpProfile
            # 腾讯tts句柄
            #  "ap-guangzhou" 该值可能为请求的服务器位置，这里为广州，可登录腾讯云控制台查看：https://console.cloud.tencent.com/api/explorer?Product=tts
            client = tts_client.TtsClient(cred, "ap-guangzhou", clientProfile)
            # 腾讯tts请求参数结构体
            req = models.TextToVoiceRequest()
            params = '{"Text":"'+text+'","VoiceType":"'+voiceType+'","SessionId":"'+str(uuid.uuid4())+'","ModelType":"1"}'
            print(params)
            req.from_json_string(params)
            # 生成语音
            resp = client.TextToVoice(req)
            # 将返回的数据转换成dict（字典类型）
            audioBase64=json.loads(resp.to_json_string())
            # 将base64的字符转换成二进制流
            stream = base64.b64decode(audioBase64["Audio"])
            print(text)
            # 打开文件
            wavfile = open("test.wav", "wb")
            # 写入文件
            wavfile.write(stream)
            # 关闭文件
            wavfile.close()
        except TencentCloudSDKException as err:
            print(err)

        # env.ini信息
    def __setApiInfo(self):
        msg = 0
        # 读取配置文件
        config = configparser.ConfigParser()
        if len(config.read("./env.ini")) == 0:
            msg = '没有配置文件'
        else:
            # 以下信息需要百度智能云生成应用时获得
            if 'Tencent_API' in config:
                if ('AppId' in config['Tencent_API']):
                    self.__appId = config['Tencent_API']['AppId'].strip()
                    if (self.__appId == ''):
                        msg = 'AppId字段是空的'
                    else:
                        msg = 0
                else:
                    msg = 'AppId字段不存在'

                if ('SecretId' in config['Tencent_API']):
                    self.__secretId = config['Tencent_API']['SecretId'].strip()
                    if (self.__secretId == ''):
                        msg = 'SecretId字段是空的'
                    else:
                        msg = 0
                else:
                    msg = 'SecretId字段不存在'

                if ('SecretKey' in config['Tencent_API']):
                    self.__secretKey = config['Tencent_API']['SecretKey'].strip()
                    if (self.__secretKey == ''):
                        msg = 'SecretKey字段是空的'
                    else:
                        msg = 0
                else:
                    msg = 'SecretKey字段不存在'
            else:
                msg = '请按照要求配置好env.ini文件'
        return msg

    def __del__(self):
        print('腾讯语音合成类使命完成')
