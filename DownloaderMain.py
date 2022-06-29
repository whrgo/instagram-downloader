import instaloader

class Downloader():
    def __init__(self, username):
        self.username = username
        self.loader = instaloader.Instaloader()

    def downloadPicture(self):
        self.loader.download_profile(self.username, profile_pic_only=True)


if __name__ == "__main__":
    instance = Downloader(str(input('id: ')))
    instance.downloadPicture()