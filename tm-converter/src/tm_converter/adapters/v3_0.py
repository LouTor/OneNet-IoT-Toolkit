from ..core.converters.base_converter import BaseConverter
from ..core.models.intermediate import *


class V30Adapter(BaseConverter):
    @classmethod
    def to_intermediate(cls, raw_data):
        intermediate_model = IntermediateModel(**raw_data)
        # print(f"中间模型内容：{intermediate_model}\n中间模型数据类型：{type(intermediate_model)}\n")
        return intermediate_model

    @classmethod
    def from_intermediate(cls, intermediate):
        output = intermediate.dict()  # 完全转为原生字典
        cls.func_type(output, "st")  # fuctionType处理 "st"/"u"
        cls.desc(output, "ept")


        return output


