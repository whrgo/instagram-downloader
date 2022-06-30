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

    def DownloadStart(self, event=None):
        instance = Downloader.Downloader(self.ID.GetValue())
        self.btnDownload.Disable()
        try:
            if self.DownloadWayChoice.GetSelection() == 0:
                Thread(target=instance.downloadProfilePicture).start()
            elif self.DownloadWayChoice.GetSelection() == 1:
                Thread(target=instance.downloadPosts).start()
                

        except instaloader.exceptions.ProfileNotExistsException as e:
            self.print(e)
            return

        except Exception as e:
            self.print(e)
            return



    def print(self, message):
        self.tbConsole.AppendText(message + "\n")


if __name__ == '__main__':
    app = wx.App()
    frame = Frame(None, '')
    app.MainLoop()