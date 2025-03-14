import unittest
from src.video_player import play_video

class TestVideoPlayer(unittest.TestCase):
    def test_play_video(self):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        try:
            play_video(url)
            success = True
        except Exception:
            success = False

        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
