## 环境

python：须3.10以上

GUI界面使用：Windows

## 功能说明

将onenet 公有云融合平台版本(fuse)与城市平台3个版本的物模型互相转换。

- 不同版本onenet平台的物模型兼容情况如下表：

|  源版本  | 目标版本3.0 | 目标版本2.x | 目标版本1.2 | 目标版本fuse |
| :------: | :---------: | :---------: | :---------: | :----------: |
| 版本3.0  |      —      |   ❌ 失败    |   ❌ 失败    |    ❌ 失败    |
| 版本2.x  |   ✅ 成功    |      —      |   ❌ 失败    |    ✅ 成功    |
| 版本1.2  |   ❌ 失败    |   ❌ 失败    |      —      |    ❌ 失败    |
| 版本fuse |   ❌ 失败    |   ❌ 失败    |   ❌ 失败    |      —       |

- 此数据处理工具实现兼容如下表：

|  源版本  | 目标版本3.0 | 目标版本2.x | 目标版本1.2 | 目标版本fuse |
| :------: | :---------: | :---------: | :---------: | :----------: |
| 版本3.0  |      —      |   ✅ 成功    |   ✅ 成功    |    ✅ 成功    |
| 版本2.x  | ✅ 无需转换  |      —      |   ✅ 成功    |  ✅ 无需转换  |
| 版本1.2  |   ✅ 成功    |   ✅ 成功    |      —      |    ✅ 成功    |
| 版本fuse |   ✅ 成功    |   ✅ 成功    |   ✅ 成功    |      —       |

##快速开始

1. 克隆仓库
```bash
git clone https://github.com/LouTor/OneNet-IoT-Toolkit.git
```

2.安装依赖
```bash
pip install -r requirements.txt
```

3.打包可执行文件(可选，界面操作)

```bash
cd tm_converter/src/tm_converter  # 进入main.py目录
pyinstaller --onefile --noconsole main.py
```
打包好的可执行文件: dist/main.exe

4.数据处理接口(可选)
`tm_converter.src.tm_converter.services.conversion_service.ConversionService,convert`

```python
input_data = load_json("原版本json文件路径")
output = ConversionService.convert(input_data, "源版本", "目标版本")
```







