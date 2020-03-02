# srt_to_speech
 srt字幕文件转换成语音
## 关于程序
    这是一个用pyton写的语音合成程序
    主要用于翻译声音
    需要srt字幕文件
    
## 模块要求
   - [pydub](http://pydub.com/)：音频处理
   - [tencentcloud-sdk-python](https://github.com/TencentCloud/tencentcloud-sdk-python)：腾讯api，百度的接口部分还没完成
   - [pysubs2](https://github.com/tkarabela/pysubs2)：srt字幕文件处理
   
## 使用方法、
    1、复制env.ini.example文件，改名为env.ini，并填充Tencent_API的接口所需数据
    2、修改字幕文件地址
        srt = SrtClass("./srt/test.srt")
    3、创建文件根目录下创建 “sound” 文件夹
    