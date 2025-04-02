from tm_converter.src.tm_converter.core.converters.version_factory import ConverterFactory
from tm_converter.src.tm_converter.services.version_detector import VersionDetector


class ConversionService:
    @staticmethod
    def convert(input_data: dict, src_version, target_version: str) -> dict:
        """
        :param input_data: json数据
        :param src_version: 源版本
        :param target_version: 目标版本
        :return:
        """
        # 检测输入版本 无需太关注
        if src_version == "自动检测源版本":
            src_version = VersionDetector.detect(input_data)
        else:
            src_version = VersionDetector.select(src_version)

        # 获取转换器
        src_converter = ConverterFactory.get_converter(src_version)
        dst_converter = ConverterFactory.get_converter(target_version)

        # 执行转换
        intermediate = src_converter.to_intermediate(input_data)
        return dst_converter.from_intermediate(intermediate)
