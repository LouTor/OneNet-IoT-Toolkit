from abc import ABC, abstractmethod
from tm_converter.src.tm_converter.core.models.intermediate import IntermediateModel


# 笔记：abstract装饰器强制子类实现抽象基类定义的方法，不提供具体实现；子类未实现抽象方法会抛出TypeError
class BaseConverter(ABC):
    @staticmethod
    def to_intermediate(raw_data: dict) -> IntermediateModel:
        intermediate_data = {
            "properties": raw_data.get("properties", []),
            "services": raw_data.get("services", []),
            "events": raw_data.get("events", [])
        }
        # print(f"中间模型内容：{intermediate_model}\n中间模型数据类型：{type(intermediate_model)}\n")
        return IntermediateModel(**intermediate_data)

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
        for section in ('properties', 'events', 'services'):
            for item in data.get(section, []):
                item['functionType'] = dst
        return data

    @staticmethod
    def desc(data, dst: str):
        """
        将desc处理为null或空字符串
        :param data: 中间格式转化而来的待输出字典
        :param dst: "ept"或"null"  desc参数的目标值
        :return: 处理后的字典
        """
        target = None if dst == "null" else ""

        def traverse(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == "desc" and v in (None, ""):
                        obj[k] = target
                    else:
                        traverse(v)
            elif isinstance(obj, list):
                for item in obj:
                    traverse(item)
            return obj

        return traverse(data)

    @staticmethod
    def step(data, dst: str):
        """
        将step处理为null或空字符串
        :param data: 中间格式转化而来的待输出字典
        :param dst: "ept"或"null"  desc参数的目标值
        :return: 处理后的字典
        """
        target = "" if dst == "ept" else None

        def traverse(obj):
            if isinstance(obj, dict):
                # 优先处理当前层级的step字段
                if "step" in obj and obj["step"] in ("", None):
                    obj["step"] = target
                # 深度遍历其他字段
                for v in obj.values():
                    traverse(v)
            elif isinstance(obj, list):
                for item in obj:
                    traverse(item)
            return obj

        return traverse(data)

    @staticmethod
    def call_type(data, dst: str):
        """
        将callType处理为完整或简写
        :param data: 中间格式转化而来的待输出字典
        :param dst: callType参数的目标值
            "simp"：s as
            "full":sync async
        :return: 处理后的字典
        """
        # 定义映射关系
        calltype_mapping = {
            "sync": "s",
            "async": "a",
            "s": "sync",
            "a": "async"
        }
        for service in data["services"]:
            ori_calltype = service["callType"]
            if dst == "simp":
                service["callType"] = calltype_mapping[ori_calltype] if ori_calltype in ["sync", "async"] else ori_calltype
            elif dst == "full":
                service["callType"] = calltype_mapping[ori_calltype] if ori_calltype in ["s", "a"] else ori_calltype
        return data

    @staticmethod
    def func_mode(data):
        """
        在中间格式上增加functionMode字段
        :param data: 中间格式转化而来的待输出字典
        :return: 处理后的字典
        """
        for section, mode in [("properties", "property"), ("events", "event"), ("services", "service")]:
            for item in data[section]:
                item["functionMode"] = mode
        return data

    @staticmethod
    def length_str(data):
        """
        递归处理所有层级的 dataType.specs.length，确保数值转为字符串
        :param data: 输入的完整物模型字典（如 v3.0.json 内容）
        :return: 转换后的字典
        """

        def process_entry(entry):
            # 处理单个条目中的 dataType
            if "dataType" in entry:
                data_type = entry["dataType"].get("type")
                specs = entry["dataType"].get("specs")

                # 处理 specs 中的 length（数值转字符串）
                if isinstance(specs, dict) and "length" in specs:
                    specs["length"] = str(specs["length"])

                # 递归处理 struct 类型中的嵌套字段
                if data_type == "struct" and isinstance(specs, list):
                    for item in specs:
                        process_entry(item)

            # 递归处理其他可能包含 dataType 的键（如 input/output/outputData）
            for key in ["properties", "services", "events", "input", "output", "outputData"]:
                if key in entry and isinstance(entry[key], list):
                    for sub_item in entry[key]:
                        process_entry(sub_item)
            return entry

        # 从根节点开始处理
        if isinstance(data, dict):
            return process_entry(data)
        return data
