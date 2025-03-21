# docs/tm-converter.md

## 功能

- 打包生成exe可执行文件类型工具；有GUI页面


- OneNet 公共平台版本、私有化部署所有版本 物模型json文件一键互转

## 启动方式

### 环境要求
- Python 3
- Windows

### 安装依赖
```bash
cd iot-converter
pip install -r requirements.txt
```

### 命令行启动
```bash
python -m iot_converter.main
```

### GUI启动（如果有图形界面）
```bash
# Windows
python -m iot_converter.main --gui

# Linux/macOS（可能需要图形环境）
DISPLAY=:0 python -m iot_converter.main --gui
```

### Docker启动
```bash
docker build -t iot-converter -f ../tools-config/Dockerfile .
docker run -it --rm iot-converter
```