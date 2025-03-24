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

##versionFactory_getConverter.py

`python -m tm-converter.tests.core.converters.versionFactory_getConverter`

测试结果：

| 版本 | 测试结果 |
| :--: | :------: |
| 3.0  |    √     |
| 2.x  |    √     |
| 1.2  |    √     |
| fuse |    √     |



















