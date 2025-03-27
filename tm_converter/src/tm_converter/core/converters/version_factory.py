from tm_converter.src.tm_converter.core.converters.adapters import *


class ConverterFactory:
    ui_ver_map = {
        "融合平台(开放平台)" : "fuse",
        "城市平台v1.2": "1.2",
        "城市平台v2.x": "2.x",
        "城市平台v3.0": "3.0",
        "fuse": "fuse",
        "1.2": "1.2",
        "2.x": "2.x",
        "3.0": "3.0"
    }
    version_map = {
        "fuse": FuseAdapter,
        "1.2": V12Adapter,
        "2.x": V2xAdapter,
        "3.0": V30Adapter
    }

    @classmethod
    def get_converter(cls, version: str) -> BaseConverter:
        ver = cls.ui_ver_map.get(version)
        adapter_class = cls.version_map.get(ver)
        if not adapter_class:
            raise ValueError(f"Unsupported version: {ver}")
        return adapter_class
