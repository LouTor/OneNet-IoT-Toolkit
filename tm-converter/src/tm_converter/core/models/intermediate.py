from pydantic import BaseModel
from typing import List, Dict, Optional


class DataType(BaseModel):
    type: str = None
    specs: Dict | List[Dict]


class PropertyModel(BaseModel):
    identifier: str
    name: str
    functionType: str
    accessMode: str
    desc: Optional[str] = None
    dataType: DataType


class ServicesModel(BaseModel):
    identifier: str
    name: str
    functionType: str
    callType: str
    desc: str
    input: Dict | List[Dict]
    output: Dict | List[Dict]


class IntermediateModel(BaseModel):
    properties: List[PropertyModel] = []
    services: List[ServicesModel] = []
    events: List[Dict] = []
