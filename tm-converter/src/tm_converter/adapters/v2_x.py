from ..core.converters.base_converter import BaseConverter
from ..core.models.intermediate import *


class V2xAdapter(BaseConverter):
    @classmethod
    def to_intermediate(cls, raw_data):
        # 处理v2.x版本特性
        return IntermediateModel(
            version=raw_data['version'],
            profile=raw_data['profile'],
            properties=[cls._convert_specs(p) for p in raw_data['properties']],
            services=raw_data['services'],
            events=raw_data['events']
        )

    @staticmethod
    def _convert_specs(prop):
        # 处理step字段null值
        if prop['dataType']['specs'].get('step') is None:
            prop['dataType']['specs']['step'] = ""
        return PropertyModel(**prop)

    @classmethod
    def from_intermediate(cls, intermediate):
        output = intermediate.dict(exclude_unset=True)
        # 保持v2.x格式
        output['profile']['stTmId'] = ""  # 添加v2.x特有字段
        return output
