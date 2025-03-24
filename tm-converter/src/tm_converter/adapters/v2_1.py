from ..core.converters.base_converter import BaseConverter
from ..core.models.intermediate import *

class V21Adapter(BaseConverter):
    def to_intermediate(self, raw_data):
        # 处理v2.x版本特性
        return IntermediateModel(
            version=raw_data['version'],
            profile=raw_data['profile'],
            properties=[self._convert_specs(p) for p in raw_data['properties']],
            services=raw_data['services'],
            events=raw_data['events']
        )

    def _convert_specs(self, prop):
        # 处理step字段null值
        if prop['dataType']['specs'].get('step') is None:
            prop['dataType']['specs']['step'] = ""
        return PropertyModel(**prop)

    def from_intermediate(self, intermediate):
        output = intermediate.dict(exclude_unset=True)
        # 保持v2.x格式
        output['profile']['stTmId'] = ""  # 添加v2.x特有字段
        return output