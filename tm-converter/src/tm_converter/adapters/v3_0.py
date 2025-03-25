from ..core.converters.base_converter import BaseConverter
from ..core.models.intermediate import *


class V30Adapter(BaseConverter):
    @staticmethod
    def to_intermediate(raw_data):
        intermediate_model = IntermediateModel(
            properties=raw_data.get('properties', []),
            services=raw_data.get('services', []),
            events=raw_data.get('events', [])
        )
        # print(f"中间模型内容：{intermediate_model}\n中间模型数据类型：{type(intermediate_model)}")
        return intermediate_model

    @classmethod
    def from_intermediate(cls, intermediate):
        # 中间模型转v3.0格式
        output = {
            "properties": intermediate.properties,
            "services": intermediate.services,
            "events": intermediate.events
        }
        # 处理functionType转换
        for prop in output['properties']:
            prop.functionType = 'st'
        return output

