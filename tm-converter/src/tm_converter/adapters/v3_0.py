from ..core.converters.base_converter import BaseConverter
from ..core.models.intermediate import *


class V30Adapter(BaseConverter):
    @classmethod
    def to_intermediate(cls, raw_data):
        # 处理v3.0特有字段到中间模型
        profile = raw_data.get('profile', {})
        # 处理video相关字段...
        '''
        # debug
        intermediate_model = IntermediateModel(
            profile=profile,
            properties=[cls._convert_property(p) for p in raw_data['properties']],
            services=raw_data.get('services', []),
            events=raw_data.get('events', [])
        )
        print(f"中间模型内容：{intermediate_model}\n中间模型数据类型：{type(intermediate_model)}")
        return intermediate_model
        '''
        return IntermediateModel(
            profile=profile,
            properties=[cls._convert_property(p) for p in raw_data['properties']],
            services=raw_data.get('services', []),
            events=raw_data.get('events', [])
        )

    @staticmethod
    def _convert_property(prop):
        # 处理v3.0的struct类型错误
        if prop['dataType']['type'] == 'struct':
            if isinstance(prop['dataType']['specs'], dict):
                # 修正为数组结构
                prop['dataType']['specs'] = [prop['dataType']['specs']]
        return PropertyModel(**prop)

    @classmethod
    def from_intermediate(cls, intermediate):
        # 中间模型转v3.0格式
        output = {
            "profile": intermediate.profile,
            "properties": [cls._format_property(p) for p in intermediate.properties]
        }
        # 处理functionType转换
        for prop in output['properties']:
            prop.functionType = 'st'
        return output

    @staticmethod
    def _format_property(prop):
        # 假设 _format_property 是一个辅助方法
        return prop
