import os.path
import wx
from tm_converter.src.tm_converter.gui_wx.ui_wx import MyFrame
from tm_converter.src.tm_converter.utils import file_utils, logger
from tm_converter.src.tm_converter.services.conversion_service import ConversionService


# 功能实现类
class FrameAction(MyFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.src_ver = None
        self.tagt_ver = None
        self.tm_path = None
        self.tm_converted_path = None
        self.tm_points_json = None
        self.tm_converted_json = None
        # self.logger = logger.setup_logger("TmConverter")

    def SelectFilePath(self, event):
        filedialog = wx.FileDialog(self, "选择物模型json文件", "", "", "*.json", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if filedialog.ShowModal() == wx.ID_OK:
            self.tm_path = filedialog.GetPath()
        try:
            self.tm_points_json = file_utils.load_json(self.tm_path)
        except ValueError as e:
            self.logger.error(f"文件加载失败：{str(e)}")
            wx.MessageBox(str(e), "错误", wx.OK | wx.ICON_ERROR)
        self.CtextModPath.SetValue(self.tm_path)

    # 转换按钮
    def StartConvert(self, event):
        self.src_ver = self.choVersion1.GetStringSelection()
        self.tagt_ver = self.choVersion2.GetStringSelection()
        self.tm_converted_json = ConversionService.convert(self.tm_points_json, self.src_ver, self.tagt_ver)
        file_name = os.path.splitext(os.path.basename(self.tm_path))[0]  # 获取完整文件名元组的元素[0] 不含拓展名的文件名
        self.tm_converted_path = os.path.join(os.path.dirname(self.tm_path), f"{self.tagt_ver}-{file_name}.json")
        file_utils.save_json(self.tm_converted_json, self.tm_converted_path)
        self.CtextSavePath.SetValue(self.tm_converted_path)

    def openFile(self, event):
        path = self.tm_converted_path
        if not path:
            wx.MessageBox("保存路径不能为空", "错误", wx.OK | wx.ICON_ERROR)
            return
        if os.path.isfile(path):
            path = os.path.dirname(path)
        if not os.path.exists(path):
            wx.MessageBox(f"路径不存在：{path}", "错误", wx.OK | wx.ICON_ERROR)
            return

        try:
            if wx.Platform == '__WXMSW__':
                os.startfile(path)
        except Exception as e:
            wx.MessageBox(f"打开路径失败：{str(e)}", "错误", wx.OK | wx.ICON_ERROR)

    def help_document(self, event):
        url = 'https://github.com/LouTor/OneNet-IoT-Toolkit/blob/main/tm_converter/README.md'
        if not wx.LaunchDefaultBrowser(url):
            wx.MessageBox("无法启动浏览器", "错误", wx.OK | wx.ICON_ERROR)

    def help_downloadAddress(self, event):
        url = 'https://github.com/LouTor/OneNet-IoT-Toolkit/blob/main/tm_converter/README.md'
        if not wx.LaunchDefaultBrowser(url):
            wx.MessageBox("无法启动浏览器", "错误", wx.OK | wx.ICON_ERROR)

    def suggestion(self, event):
        url = 'https://docs.qq.com/form/page/DSG9ta29LVFVpbWJZ'
        if not wx.LaunchDefaultBrowser(url):
            wx.MessageBox("无法启动浏览器", "错误", wx.OK | wx.ICON_ERROR)
