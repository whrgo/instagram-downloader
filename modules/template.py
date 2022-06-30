import wx


class InstagramDownloader(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 400))

        self.panel = wx.Panel(self, -1)

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("instagram downloader")
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        ...
        self.Layout()


class MyApp(wx.App):
    def OnInit(self):
        self.Window = InstagramDownloader(None, wx.ID_ANY, "", )
        self.SetTopWindow(self.Window)
        self.Window.Show()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()