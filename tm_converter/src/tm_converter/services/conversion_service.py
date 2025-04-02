from tm_converter.src.tm_converter.core.converters.version_factory import ConverterFactory
from tm_converter.src.tm_converter.services.version_detector import VersionDetector


class ConversionService:
    @staticmethod
    def convert(input_data: dict, src_version, target_version: str) -> dict:
        """
        :param input_data: json数据
        :param src_version: 源版本，可输入：
            "自动检测源版本"
            "融合平台(开放平台)"
            "城市平台v1.2"
            "城市平台v2.x"
            "城市平台v3.0"
            "fuse"
            "1.2"
            "2.x"
            "3.0"
        :param target_version: 目标版本，输入：
            "fuse"
            "1.2"
            "2.x"
            "3.0"
        :return:
        """
        if src_version == "自动检测源版本":
            src_version = VersionDetector.detect(input_data)
        else:
            src_version = VersionDetector.select(src_version)

        src_converter = ConverterFactory.get_converter(src_version)
        dst_converter = ConverterFactory.get_converter(target_version)

        intermediate = src_converter.to_intermediate(input_data)
        return dst_converter.from_intermediate(intermediate)
