import wx
import instaloader
from threading import Thread
import DownloaderMain as Downloader  # Load Downloader functions
from modules.template import InstagramDownloader

class Frame(InstagramDownloader):
    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title)

        self.__do_bind()

        self.Show()
        self.Centre()


    def __do_bind(self):
        self.btnDownload.Bind(wx.EVT_BUTTON, self.DownloadStart)
        self.btnDownloadStop.Bind(wx.EVT_BUTTON, self.DownloadStop)

    def DownloadStart(self, event=None):
        instance = Downloader.Downloader(self.ID.GetValue())
        self.btnDownload.Disable()
        self.btnDownloadStop.Enable()
        try:
            if self.DownloadWayChoice.GetSelection() == 0:
                Thread(target=instance.downloadProfilePicture).start()
            elif self.DownloadWayChoice.GetSelection() == 1:
                Thread(target=instance.downloadPosts).start()
                

        except instaloader.exceptions.ProfileNotExistsException as e:
            print("Error", e, wx.ICON_WARNING)
            return

        except Exception as e:
            print("Error", e, wx.ICON_WARNING)
            return


    def DownloadStop(self, event=None):
        
        self.btnDownload.Enable()
        self.btnDownloadStop.Disable()



    def print(self, title, message, props=None):
        wx.MessageBox(title,  message, props)


if __name__ == '__main__':
    app = wx.App()
    frame = Frame(None, '')
    app.MainLoop()