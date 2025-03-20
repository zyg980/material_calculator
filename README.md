# 金峡能源材料计算器

## 功能特点
- 支持计算长方体、圆柱体和圆管的质量
- 内置多种常用材料密度
- 直观的用户界面
- 实时计算结果

## 开发环境
- Python 3.11
- Kivy 2.3.0
- Buildozer 1.5.0

## 安装步骤
```bash
# 创建并激活虚拟环境
python -m venv venv
.\venv\Scripts\activate

# 安装依赖
pip install kivy
```

## 运行方法
```bash
cd src
python main.py
```

## 项目结构
material_calculator/
├── src/
│   └── main.py
├── assets/
│   └── icon.png
├── buildozer.spec
└── README.md

## 预览运行

```powershell
# 确保在虚拟环境中
.\venv\Scripts\activate

# 运行程序
python src/main.py
```