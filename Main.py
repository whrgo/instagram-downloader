import wx
from modules import template as tmpl

class MyFrame(tmpl.InstagramDownloader):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show()
        self.Centre()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, '')
    app.MainLoop()