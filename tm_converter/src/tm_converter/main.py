import wx
from tm_converter.src.tm_converter.gui_wx.ui_funcs import FrameAction

if __name__ == "__main__":
    app = wx.App()
    frame = FrameAction(None)
    frame.Show()
    app.MainLoop()
