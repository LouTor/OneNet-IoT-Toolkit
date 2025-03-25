from ..core.converters.base_converter import BaseConverter
from ..core.models.intermediate import *


class FuseAdapter(BaseConverter):
    @classmethod
    def to_intermediate(cls, raw_data):
        # 处理FUSE特有字段（如combs）
        return IntermediateModel(
            version=raw_data.get('version'),
            profile=raw_data['profile'],
            properties=[cls._convert_property(p) for p in raw_data['properties']],
            services=raw_data['services'],
            events=raw_data['events'],
            combs=raw_data.get('combs', [])
        )

    @staticmethod
    def _convert_property(prop):
        # 处理FUSE的required字段
        if 'required' in prop:
            del prop['required']
        return PropertyModel(**prop)

    @classmethod
    def from_intermediate(cls, intermediate):
        output = intermediate.dict(exclude_unset=True)
        # 还原FUSE特有结构
        output['combs'] = []
        for prop in output['properties']:
            prop['functionType'] = 'u'  # 恢复旧版本值
            prop['required'] = False
        return output
