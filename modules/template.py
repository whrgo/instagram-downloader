import wx


class InstagramDownloader(wx.Frame):
    def __init__(self, *args, **kwds):
        # Initializing the frame
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 400))

        # Creating the panel
        self.panel = wx.Panel(self, -1)

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        # creating the input field (id)
        self.lbID = wx.StaticText(self.panel, -1, "ID: ")
        self.ID = wx.TextCtrl(self.panel, -1, "")

        # creating the button
        self.btnDownload = wx.Button(self.panel, -1, "Download posts")
        self.btnDownloadStop = wx.Button(self.panel, -1, "Stop downloading")
        self.btnDownloadStop.Disable() # Disable the button until the download is started

        # creating the settings for download
        self.DownloadWayChoice = wx.Choice(self.panel, -1, choices=["Download only profile picture", "Download all posts"])
        self.DownloadWayChoice.SetSelection(0)
        self.DownloadWayChoice.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))

        # creating the Console
        self.tbConsole = wx.TextCtrl(self.panel, -1, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.tbConsole.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Consolas"))


        # Default properties
        self.SetTitle("instagram downloader")
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        # Creating the sizer
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)


        # Creating the sizer for the input field
        InputIDGrid = wx.FlexGridSizer(1, 2, 0, 0)
        InputIDGrid.Add(self.lbID, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        InputIDGrid.Add(self.ID, 0, wx.EXPAND, 0)
        InputIDGrid.AddGrowableCol(1)
        sizer_2.Add(InputIDGrid, 0, wx.EXPAND, 0)


        # Creating the sizer for the button
        sizer_2.Add(self.DownloadWayChoice, 0, wx.ALL | wx.EXPAND, 10)

        # Creating the sizer for the download buttons
        button_grid = wx.GridSizer(1, 2, 0, 0)
        button_grid.Add(self.btnDownload, 0, wx.EXPAND, 0)
        button_grid.Add(self.btnDownloadStop, 0, wx.EXPAND, 0)
        sizer_2.Add(button_grid, 0, wx.EXPAND, 0)

        # adding tbConsole to the sizer
        sizer_2.Add(self.tbConsole, 1, wx.EXPAND, 0)

        self.panel.SetSizer(sizer_2)
        
        sizer_1.Add(self.panel, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer_1)
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