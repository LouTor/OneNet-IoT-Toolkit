from ..core.converters.base_converter import BaseConverter
from ..core.models.intermediate import *


class V12Adapter(BaseConverter):
    @classmethod
    def to_intermediate(cls, raw_data):
        # 处理v1.2特有逻辑（如callType简写）
        processed = IntermediateModel(
            # properties=[cls._convert_property(p) for p in raw_data['properties']],
            services=V12Adapter._convert_services(raw_data['services']),
            events=raw_data['events']
        )
        return processed

    @staticmethod
    def _convert_property(properties):
        pass

    @staticmethod
    def _convert_services(services):
        for service in services:
            # 转换callType简写
            if service.get('callType') == 's':
                service['callType'] = 'sync'
        return services

    @classmethod
    def from_intermediate(cls, intermediate):
        '''
        output = intermediate.dict(exclude_unset=True)
        # 还原v1.2格式
        for service in output['services']:
            service.callType = 's'  # 恢复简写
            service.functionType = 'u'
        return output
        '''
        return 0
