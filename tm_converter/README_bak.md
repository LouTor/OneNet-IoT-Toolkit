## 环境

python：须3.10以上

## 功能介绍

### 功能说明
将onenet 公有云融合平台版本(fuse)与城市平台3个版本的物模型互相转换。

不同版本onenet平台的物模型兼容情况如下表：

|  源版本  | 目标版本3.0 | 目标版本2.x | 目标版本1.2 | 目标版本fuse |
| :------: | :---------: | :---------: | :---------: | :----------: |
| 版本3.0  |      —      |   ❌ 失败    |   ❌ 失败    |    ❌ 失败    |
| 版本2.x  |   ✅ 成功    |      —      |   ❌ 失败    |    ✅ 成功    |
| 版本1.2  |   ❌ 失败    |   ❌ 失败    |      —      |    ❌ 失败    |
| 版本fuse |   ❌ 失败    |   ❌ 失败    |   ❌ 失败    |      —       |

此数据处理工具实现兼容如下表：

|  源版本  | 目标版本3.0 | 目标版本2.x | 目标版本1.2 | 目标版本fuse |
| :------: | :---------: | :---------: | :---------: | :----------: |
| 版本3.0  |      —      |   ✅ 成功    |   ✅ 成功    |    ✅ 成功    |
| 版本2.x  | ✅ 无需转换  |      —      |   ✅ 成功    |  ✅ 无需转换  |
| 版本1.2  |   ✅ 成功    |   ✅ 成功    |      —      |    ✅ 成功    |
| 版本fuse |   ✅ 成功    |   ✅ 成功    |   ✅ 成功    |      —       |

##快速开始

1. 克隆仓库
```bash
git clone https://github.com/yourname/repository-root.git
```

2. 安装工具A（IoT转换器）
```bash
cd repository-root/iot-core
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
pyinstaller --onefile src/iot_converter/example.py
```





