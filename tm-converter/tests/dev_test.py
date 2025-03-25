from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Optional
from ..src.tm_converter.utils.file_utils import load_json

# src_data = load_json("tm-converter/tests/json_tms/v3.0.json")
src_data = {
        "properties": [{
            "identifier": "temp",
            "name": "温度",
            "functionType": "u",
            "accessMode": "rw",
            "functionMode": "property",
            "desc": None,
            "dataType": {
                "type": "float",
                "specs": {
                    "min": "0",
                    "max": "99999",
                    "unit": None,
                    "step": None
                }
            }
        }],
        "events": [],
        "services": []
}


class DataSpecs(BaseModel):
    # 启用忽略多余字段的配置
    model_config = ConfigDict(extra='ignore')  # 替换 Extra.ignore
    # 通用specs结构
    max: Optional[str] = None
    min: Optional[str] = None
    step: Optional[str] = None
    unit: Optional[str] = None
    length: Optional[int] = None
    define: Optional[List[Dict]] = None
    # 其他可能字段...
    @classmethod
    def from_raw_data(cls, raw_data: dict) -> "DataSpecs":
        """
        根据原始数据创建 DataSpecs 对象，区分 None 和缺失字段。
        """
        # 记录原始数据中存在的字段
        raw_keys = set(raw_data.keys())

        # 过滤掉原始数据中不存在的字段
        filtered_data = {
            key: value for key, value in raw_data.items()
            if key in cls.model_fields  # 替换 __fields__
        }

        # 创建模型实例
        instance = cls(**filtered_data)

        # 动态删除未在原始数据中出现的字段
        for field_name in list(instance.model_fields):  # 替换 __fields__
            if field_name not in raw_keys:
                delattr(instance, field_name)

        return instance


class DataType(BaseModel):
    type: str = None
    specs: DataSpecs | List[Dict]  # 兼容数组/对象

class PropertyModel(BaseModel):
    identifier: str
    name: str
    functionType: str
    accessMode: str
    desc: Optional[str] = None
    dataType: DataType

class IntermediateModel(BaseModel):
    # version: Optional[str] = None
    # profile: Dict = None
    properties: List[PropertyModel] = []
    services: List[Dict] = []
    events: List[Dict] = []
    #combs: Optional[List] = None

# intermediate_model = IntermediateModel(properties=src_data.get('properties', []))
# print(f"{intermediate_model}\n{type(intermediate_model)}")

raw_data = {
    "max": "100",
    "step": None,
    "unknown_field": "this will be ignored"
}
data_specs = DataSpecs.from_raw_data(raw_data)
print(data_specs)
print(data_specs.model_dump())