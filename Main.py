import wx
import DownloaderMain as Downloader  # Load Downloader functions
from modules import template as tmpl # Load wx.Frame template

class Frame(tmpl.InstagramDownloader):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 200))
        
        self.Show()
        self.Centre()


if __name__ == '__main__':
    app = wx.App()
    frame = Frame(None, '')
    app.MainLoop()