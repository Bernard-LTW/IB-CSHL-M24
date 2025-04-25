import pytest
from Quiz052 import MovieDownloader

def test_calculate_download_time():
    downloader = MovieDownloader(download_speed=10)
    movie_size = 1500 * 1024 * 1024  # 1500 MB
    assert downloader.calculate_download_time(movie_size) == "2 minutes 30 seconds"

    downloader = MovieDownloader(download_speed=5)
    movie_size = 500 * 1024 * 1024  # 500 MB
    assert downloader.calculate_download_time(movie_size) == "1 minutes 40 seconds"

def test_download_speed_validation():
    with pytest.raises(ValueError, match=r"Download speed must be greater than 0"):
        downloader = MovieDownloader(download_speed=0)
    with pytest.raises(ValueError, match=r"Download speed must be greater than 0"):
        downloader = MovieDownloader(download_speed=-10)

def test_movie_size_validation():
    downloader = MovieDownloader(download_speed=10)
    with pytest.raises(ValueError, match=r"Movie size must be greater than 0"):
        downloader.calculate_download_time(0)
    with pytest.raises(ValueError, match=r"Movie size must be greater than 0"):
        downloader.calculate_download_time(-100)
