#2023-03-03 Quiz052.md
class MovieDownloader:
    def __init__(self, download_speed):
        if download_speed <= 0:
            raise ValueError("Download speed must be greater than 0")
        self.download_speed = download_speed

    def calculate_download_time(self, movie_size):
        if movie_size <= 0:
            raise ValueError("Movie size must be greater than 0")
        download_time_seconds = movie_size / (self.download_speed * 1024 * 1024)
        print(download_time_seconds)
        minutes, seconds = divmod(download_time_seconds, 60)
        return f"{int(minutes)} minutes {int(seconds)} seconds"
