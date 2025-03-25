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

## Adapters
`python -m tm-converter.tests.adapters.V30Adapter`

`python -m tm-converter.tests.adapters.VFuseAdapter` ...

未处理转换表：

|  源版本  | 目标版本3.0 | 目标版本2.x | 目标版本1.2 | 目标版本fuse |
| :------: | :---------: | :---------: | :---------: | :----------: |
| 版本3.0  |      —      |             |             |              |
| 版本2.x  |   ✅ 成功    |      —      |             |              |
| 版本1.2  |   ❌ 失败    |             |      —      |              |
| 版本fuse |   ❌ 失败    |             |             |      —       |

处理后转换表：

|  源版本  | 目标版本3.0 | 目标版本2.x | 目标版本1.2 | 目标版本fuse |
| :------: | :---------: | :---------: | :---------: | :----------: |
| 版本3.0  |      —      |   ✅ 成功    | ⚠️ 部分错误  |    ❌ 失败    |
| 版本2.x  |   ✅ 成功    |      —      |   ❌ 失败    |  ⚠️ 部分错误  |
| 版本1.2  | ⚠️ 部分错误  |   ❌ 失败    |      —      |    ✅ 成功    |
| 版本fuse |   ❌ 失败    | ⚠️ 部分错误  |   ✅ 成功    |      —       |
















