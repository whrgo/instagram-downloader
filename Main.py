import wx
import DownloaderMain as Downloader  # Load Downloader functions
from modules.template import InstagramDownloader

class Frame(InstagramDownloader):
    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title)

        self.__do_Bind()

        self.Show()
        self.Centre()
    
    def __do_Bind(self):
        self.btnDownload.Bind(wx.EVT_BUTTON, self.DownloadStart)
        self.btnDownloadStop.Bind(wx.EVT_BUTTON, self.DownloadStop)

    def DownloadStart(self, event):
        self.btnDownload.Disable()
        self.btnDownloadStop.Enable()

    def DownloadStop(self, event):
        self.btnDownload.Enable()
        self.btnDownloadStop.Disable()


if __name__ == '__main__':
    app = wx.App()
    frame = Frame(None, '')
    app.MainLoop()