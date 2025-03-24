from ...adapters import FuseAdapter, V12Adapter, V21Adapter, V30Converter
from .base_converter import BaseConverter


class ConverterFactory:
    version_map = {
        "fuse": FuseAdapter,
        "1.2": V12Adapter,
        "2.x": V21Adapter,
        "3.0": V30Converter
    }

    @classmethod
    def get_converter(cls, version: str) -> BaseConverter:
        adapter_class = cls.version_map.get(version)
        print(f"adapter类名称：{adapter_class}\nadapter数据类型：{type(adapter_class)}")
        if not adapter_class:
            raise ValueError(f"Version Error: {version}")
        return adapter_class()
