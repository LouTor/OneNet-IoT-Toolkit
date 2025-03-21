from abc import ABC, abstractmethod
from ..models.intermediate import IntermediateModel

# 笔记：abstract装饰器强制子类实现抽象基类定义的方法，不提供具体实现；子类未实现抽象方法会抛出TypeError
class BaseConverter(ABC):
    @abstractmethod
    def to_intermediate(self, raw_data: dict) -> IntermediateModel:
        pass

    @abstractmethod
    def from_intermediate(self, intermediate: IntermediateModel) -> dict:
        pass
