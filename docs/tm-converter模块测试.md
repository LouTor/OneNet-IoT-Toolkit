# 物模型转换工具测试记录

25/3/24 刘涛

## VersionDetector.py

`python -m tm-converter.tests.services.versionDetector`

input path:`tm-converter/tests/json_tms/xxx.json`

测试结果：

| 版本 | 测试结果 |
| :--: | :------: |
| 3.0  |    √     |
| 2.x  |    √     |
| 1.2  |    √     |
| fuse |    √     |

## versionFactory_getConverter.py

`python -m tm-converter.tests.core.converters.versionFactory_getConverter`

测试结果：

| 版本 | 测试结果 |
| :--: | :------: |
| 3.0  |    √     |
| 2.x  |    √     |
| 1.2  |    √     |
| fuse |    √     |

## V30Converter
`python -m tm-converter.tests.adapters.V30Converter`

### Error：circular import：

修改version_factory，**动态导入**adapters模块解决

### Error：Field required

原因：

pydantic库报错；`IntermediateModel`模型初始化时缺失`services`和`events`两个必填字段，Pydantic在数据验证过程中发现缺失。

解决：

在def to_intermediate内创建实例时加上        services=src_data.get('services', []),         events=src_data.get('events', []),

### TypeError: 'PropertyModel' object does not support item assignment

原因：

intermediateModel是pydantic模型，不能使用字典的形式赋值。修改from_intermediate中的赋值方式即可。

### 测试结果：

输出intermediate model(pydantic Model)和output data(dict)内容
















