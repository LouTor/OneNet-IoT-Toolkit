## 版本更新记录
*******************************************
25/5/6 v2.1
1.修复目标版本为3.0时，字符串功能点length长度超过限制长度的问题
2.修正帮助文档的github链接 正确指向README文档
*******************************************
25/3/30 v2.0
1.代码重构：
    - 模块化重构，分为UI模块、转换逻辑模块、服务层调用模块、工具模块，增加可拓展性
    - 转换逻辑优化，采用源版本 -> 中间版本 -> 目标版本的结构，通过中间版本减少多个版本下的代码冗余、复杂度
2.UI界面优化，增加帮助链接(github-readme)、问题反馈
3.功能更新：
    - 支持融合平台以及城市平台v1.2-v3.0 4个版本之间物模型互转
    - 新增输入版本自动检测功能，无需用户确认源版本即可转换目标版本

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

## 快速开始

1. 克隆仓库
```bash
git clone https://github.com/LouTor/OneNet-IoT-Toolkit.git
```

2.安装依赖
```bash
cd tm_converter
pip install -r requirements.txt
```

3.打包可执行文件(可选，界面操作)

```bash
cd tm_converter/src/tm_converter
pyinstaller --onefile --noconsole main.py
```
pyinstaller可能出现包缺失报错，原因是pyinstaller的动态导入识别问题，解决方式如下：
在main.spec中的`a = Analysis`下加入`hiddenimports=['pydantic']`后重新打包：`pyinstaller main.spec`

打包好的可执行文件: dist/main.exe

4.数据处理接口(可选)
`tm_converter.src.tm_converter.services.conversion_service.ConversionService.convert`

```python
from tm_converter.src.tm_converter.services.conversion_service import ConversionService
from tm_converter.src.tm_converter.utils.file_utils import load_json

input_data = load_json("原版本json文件路径")
output = ConversionService.convert(input_data, "源版本", "目标版本")
```
参数详见方法注释
