from .adapters import *


class ConverterFactory:
    version_map = {
        "fuse": FuseAdapter,
        "1.2": V12Adapter,
        "2.x": V2xAdapter,
        "3.0": V30Adapter
    }

    @classmethod
    def get_converter(cls, version: str) -> BaseConverter:
        adapter_class = cls.version_map.get(version)
        if not adapter_class:
            raise ValueError(f"Unsupported version: {version}")
        return adapter_class
