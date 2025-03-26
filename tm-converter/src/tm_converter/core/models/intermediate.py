from pydantic import BaseModel, Extra
from typing import List, Dict, Optional


class DataTypeSpecs(BaseModel):
    # 允许动态字段
    class Config:
        extra = Extra.allow


class DataType(BaseModel):
    type: str
    specs: Dict | List[Dict] | DataTypeSpecs


class PropertyModel(BaseModel):
    identifier: str
    name: str
    functionType: str
    accessMode: str
    desc: Optional[str] = None
    dataType: DataType


class EventModel(BaseModel):
    identifier: str
    name: str
    functionType: str
    eventType: str
    outputData: Dict | List[Dict]
    desc: Optional[str] = None


class ServicesModel(BaseModel):
    identifier: str
    name: str
    functionType: str
    callType: str
    desc: Optional[str] = None
    input: Dict | List[Dict]
    output: Dict | List[Dict]


class IntermediateModel(BaseModel):
    properties: List[PropertyModel] = []
    services: List[ServicesModel] = []
    events: List[EventModel] = []
