from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
import mathe = material_calculator

# 在运行程序前添加
Window.size = (360, 640)  # 模拟手机屏幕尺寸

# 在 Google Colab 中运行的代码
# 安装 buildozer
!pip install buildozer

# 安装必要的依赖
!apt-get update
!apt-get install -y python3-pip build-essential git python3 python3-dev \
    ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# 创建项目目录
!mkdir -p material_calculator/src/assets

# 上传必要文件
from google.colab import files
print("请上传 main.py 文件")
uploaded = files.upload()  # 上传 main.py

print("请上传 buildozer.spec 文件")
uploaded = files.upload()  # 上传 buildozer.spec

print("请上传 msyh.ttc 字体文件")
uploaded = files.upload()  # 上传字体文件

# 移动文件到正确位置
!mv main.py material_calculator/src/
!mv buildozer.spec material_calculator/
!mv msyh.ttc material_calculator/src/assets/

# 切换到项目目录
%cd material_calculator

# 构建 APK
!buildozer android debug

# 下载生成的 APK
files.download('bin/material_calculator-0.1-debug.apk')

[app]
title = 金峡能源材料计算器
package.name = material_calculator
package.domain = org.jinxia
source.dir = src
source.include_exts = py,png,jpg,kv,atlas,ttc
version = 0.1

# 应用程序要求
requirements = python3,kivy

# 界面设置
orientation = portrait
fullscreen = 0

# Android 特定设置
android.permissions = INTERNET
android.arch = armeabi-v7a
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.bootstrap = sdl2
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1