from core.converters.base_converter import BaseConverter
from core.models.intermediate import *


class V30Converter(BaseConverter):
    def to_intermediate(self, raw_data):
        # 处理v3.0特有字段到中间模型
        profile = raw_data.get('profile', {})
        # 处理video相关字段...

        return IntermediateModel(
            profile=profile,
            properties=[self._convert_property(p) for p in raw_data['properties']],
            # ...其他字段转换
        )

    def _convert_property(self, prop):
        # 处理v3.0的struct类型错误
        if prop['dataType']['type'] == 'struct':
            if isinstance(prop['dataType']['specs'], dict):
                # 修正为数组结构
                prop['dataType']['specs'] = [prop['dataType']['specs']]
        return PropertyModel(**prop)

    def from_intermediate(self, intermediate):
        # 中间模型转v3.0格式
        output = {
            "profile": intermediate.profile,
            "properties": [self._format_property(p) for p in intermediate.properties]
        }
        # 处理functionType转换
        for prop in output['properties']:
            prop['functionType'] = 'st'
        return output
