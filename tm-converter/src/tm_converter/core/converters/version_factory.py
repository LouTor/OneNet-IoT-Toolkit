# version_factory.py
from importlib import import_module
from .base_converter import BaseConverter

class ConverterFactory:
    version_map = {
        "fuse": "FuseAdapter",
        "1.2": "V12Adapter",
        "2.x": "V21Adapter",
        "3.0": "V30Converter"
    }

    @classmethod
    def get_converter(cls, version: str) -> BaseConverter:
        adapter_class_name = cls.version_map.get(version)
        if not adapter_class_name:
            raise ValueError(f"Version Error: {version}")
        # 动态导入adapters模块
        adapter_module = import_module("tm_converter.adapters")
        adapter_class = getattr(adapter_module, adapter_class_name)
        return adapter_class()