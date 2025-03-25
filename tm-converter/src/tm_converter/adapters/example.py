import os.path
import wx
from noname import Frame
import json
# import multiprocessing


# 功能实现类
class FrameAction(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.ver = None
        self.tm_path = None
        self.tm_converted_path = None
        self.tm_points_json = None
        self.tm_converted_json = None

    # 打开文件 获取路径并返回json对象
    def _load_json(self):
        if self.tm_points_json is None:
            with open(self.tm_path, 'r', encoding='utf-8') as tm_file:
                tm_points_json = json.load(tm_file)
        return tm_points_json

    # 按钮选择文件 与 文本框显示路径
    def SelectFilePath(self, event):
        filedialog = wx.FileDialog(self, "选择物模型json文件", "", "", "*.json", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        # 选择文件 获取路径
        if filedialog.ShowModal() == wx.ID_OK:
            self.tm_path = filedialog.GetPath()
            print(self.tm_path)  # debug

            data = self._load_json()

            # 确认版本
            if self.choVersion2.GetStringSelection() == "城市平台v1.2":
                self.ver = "v1.2"
            elif self.choVersion2.GetStringSelection() == "城市平台v2.x":
                self.ver = "v2.x"

            # 获取新文件路径
            file_name = os.path.splitext(os.path.basename(self.tm_path))[0]  # 获取完整文件名元组的元素[0] 不含拓展名的文件名
            self.tm_converted_path = os.path.join(os.path.dirname(self.tm_path), f"{self.ver}-{file_name}.json")

            # 更新显示 原文件与新文件路径
            self.CtextModPath.SetValue(self.tm_path)

    # 按钮 开始转换
    def StartConvert(self, event):
        # 打开原json文件
        data = self._load_json()

        # 处理字段
        if self.ver == 'v1.2':
            self.tm_converted_json = ConVert.Convert_v12(data)
        elif self.ver == 'v2.x':
            self.tm_converted_json = ConVert.Convert_v2x(data)

        with open(self.tm_converted_path, 'w', encoding='utf-8') as tm_file_converted:
            json.dump(self.tm_converted_json, tm_file_converted, ensure_ascii=False, indent=2)

        self.CtextSavePath.SetValue(self.tm_converted_path)

    def openFile(self, event):
        os.system(self.tm_converted_path)

    def help_document(self, event):
        url = 'http://106.53.172.65/download/tool/%E7%89%A9%E6%A8%A1%E5%9E%8B%E8%BD%AC%E6%8D%A2%E5%B7%A5%E5%85%B7/readme.txt'

    def help_downloadAddress(self, event):
        pass

    def suggestion(self, event):
        pass


class ConVert:
    @staticmethod
    def Convert_v12(data):
        converted_data = DataProcessor.del_required(data)
        converted_data = DataProcessor.svc_del_required(converted_data)
        converted_data = DataProcessor.svc_chag_calltype(converted_data)
        converted_data = DataProcessor.chag_len_str(converted_data)

        return converted_data

    @staticmethod
    def Convert_v2x(data):

        return data  # 替换为实际的处理逻辑


class DataProcessor:

    # prop
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
