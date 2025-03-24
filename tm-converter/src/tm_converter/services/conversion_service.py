# 服务层调用 暴露接口为convert
from ..core.converters import ConverterFactory
from .version_detector import VersionDetector


class ConversionService:
    @staticmethod
    def convert(input_data: dict, target_version: str) -> dict:
        # 检测输入版本 无需太关注
        src_version = VersionDetector.detect(input_data)
        print(src_version)

        # 获取转换器
        src_converter = ConverterFactory.get_converter(src_version)
        dst_converter = ConverterFactory.get_converter(target_version)

        # 执行转换
        intermediate = src_converter.to_intermediate(input_data)
        return dst_converter.from_intermediate(intermediate)
