COLAB_NOTEBOOK_CONTENT = '''
# 安装 buildozer
!pip install buildozer

# 安装依赖
!apt-get update
!apt-get install -y python3-pip build-essential git python3 python3-dev \\
    ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \\
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# 创建项目目录
!mkdir -p material_calculator/src/assets

# 上传文件
from google.colab import files
print("上传 main.py...")
main_py = files.upload()

print("上传 buildozer.spec...")
spec = files.upload()

print("上传字体文件...")
font = files.upload()

# 移动文件
!mv main.py material_calculator/src/
!mv buildozer.spec material_calculator/
!mkdir -p material_calculator/src/assets
!mv msyh.ttc material_calculator/src/assets/

# 构建
%cd material_calculator
!buildozer android debug

# 下载 APK
files.download('bin/material_calculator-0.1-debug.apk')
'''

print("请按以下步骤操作：")
print("1. 打开 Google Colab: https://colab.research.google.com")
print("2. 创建新笔记本")
print("3. 复制以下代码到笔记本中：")
print("\n" + COLAB_NOTEBOOK_CONTENT)
print("\n4. 按顺序运行代码")