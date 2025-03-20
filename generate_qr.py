import qrcode
import os

def generate_qr():
    # APK 文件路径
    apk_path = 'bin/material_calculator-0.1-debug.apk'
    
    # 创建二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # 添加数据（这里可以是下载链接或其他分享方式）
    qr.add_data("file://" + os.path.abspath(apk_path))
    qr.make(fit=True)

    # 创建图像并保存
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("material_calculator_qr.png")

if __name__ == "__main__":
    generate_qr()

# 安装依赖
!pip install buildozer
!apt-get update
!apt-get install -y python3-pip build-essential git python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# 上传文件
from google.colab import files
files.upload()  # 上传 main.py, buildozer.spec 和其他必要文件

# 构建 APK
!buildozer android debug

# 下载 APK
files.download('bin/material_calculator-0.1-debug.apk')

# 生成二维码
!pip install qrcode pillow
!python generate_qr.py
files.download('material_calculator_qr.png')