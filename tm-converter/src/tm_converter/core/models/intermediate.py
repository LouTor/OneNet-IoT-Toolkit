from pydantic import BaseModel
from typing import List, Dict, Optional


class DataSpecs(BaseModel):
    # 通用specs结构
    max: Optional[str] = None
    min: Optional[str] = None
    step: Optional[str] = None
    unit: Optional[str] = None
    length: Optional[int] = None
    define: Optional[List[Dict]] = None


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
