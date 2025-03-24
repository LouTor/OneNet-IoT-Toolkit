# 暂未开发完成，仅供参考，即将更新

##快速开始

1. 克隆仓库
```bash
git clone https://github.com/yourname/repository-root.git
```

2. 安装工具A（IoT转换器）
```bash
cd repository-root/iot-converter
pip install -r requirements.txt
```

3. 运行程序
```bash
# 命令行模式
python -m iot_converter.main

# GUI模式（Windows）
python -m iot_converter.main --gui
```

4. 开发测试
```bash
# 运行所有测试
pytest tests/

# 生成可执行文件（Windows）
pyinstaller --onefile src/iot_converter/main.py
```

