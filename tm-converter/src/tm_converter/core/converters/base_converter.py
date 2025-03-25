from abc import ABC, abstractmethod
from ..models.intermediate import IntermediateModel


# 笔记：abstract装饰器强制子类实现抽象基类定义的方法，不提供具体实现；子类未实现抽象方法会抛出TypeError
class BaseConverter(ABC):
    @classmethod
    @abstractmethod
    def to_intermediate(cls, raw_data: dict) -> IntermediateModel:
        pass

    @classmethod
    @abstractmethod
    def from_intermediate(cls, intermediate: IntermediateModel) -> dict:
        pass

    @staticmethod
    def func_type(data, dst: str):
        """
        :param data: 中间格式转化而来的待输出字典
        :param dst: "st"或"u"  functionType参数的目标值
        :return: 处理后的字典
        """
        for prop in data["properties"]:
            prop["functionType"] = dst
        return data

    @staticmethod
    def desc(data, dst: str):
        """
        将desc处理为null或空字符串
        :param data: 中间格式转化而来的待输出字典
        :param dst: "ept"或"null"  desc参数的目标值
        :return: 处理后的字典
        """
        if dst not in ("null", "ept"):
            raise ValueError("Invalid dst value. Must be 'null' or 'ept'.")

        target = None if dst == "null" else ""

        def process_node(node):
            if isinstance(node, dict):
                for key in list(node.keys()):
                    if key == "desc":
                        if node[key] in (None, ""):
                            node[key] = target
                    else:
                        process_node(node[key])
            elif isinstance(node, list):
                for item in node:
                    process_node(item)
            return node

        process_node(data)
        return data

    @staticmethod
    def del_required(data):
        for prop in data.get('properties', []):
            prop.pop('required', None)
            prop.pop('buffer', None)

        for eve in data.get('events', []):
            eve.pop('required', None)
        return data

    @staticmethod
    def chag_len_str(data):
        for prop in data.get('properties', []):
            try:
                for item in prop['dataType']['specs']:
                    item['specs']['length'] = str(item['specs']['length'])
                try:
                    prop['dataType']['specs']['length'] = str(prop['dataType']['specs']['length'])
                except:
                    pass
            except:
                pass

        for eve in data.get('events', []):
            try:
                for item in eve['outputData']['specs']:
                    item['specs']['length'] = str(item['specs']['length'])
                    try:
                        eve['outputData']['specs']['length'] = str(eve['outputData']['specs']['length'])
                    except:
                        pass
            except:
                pass
        return data

    # service
    @staticmethod
    def svc_del_required(data):
        for svc in data.get('services', []):
            svc["callType"] = 's'
            svc.pop('required', None)
        return data

    @staticmethod
    def svc_chag_calltype(data):
        for svc in data.get('services', []):
            svc["callType"] = 's'
        return data

