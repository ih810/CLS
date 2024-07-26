import unittest
import os
import tempfile
from src.audio.extractor import extract_audio, get_audio_duration
from src.utils.file_operation import is_video_file, safe_file_name

class TestAudioExtractor(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_is_video_file(self):
        self.assertTrue(is_video_file('test.mp4'))

    def test_safe_file_name(self):
        self.assertEqual(safe_file_name("test<file>.mp4"), "test_file_.mp4")
        self.assertEqual(safe_file_name('test:file?.mp4'), "test_file_.mp4")

    @unittest.skip("Requires actual video file")
    def test_extract_audio(self):
        input_file = os.path.join(self.test_dir, "test_video.mp4")
        output_file = os.path.join(self.test_dir, "test_audio.wav")
        
        extract_audio(input_file, output_file)
        self.assertTrue(os.path.exists(output_file))

    @unittest.skip("Requires actual audio file")
    def test_get_audio_duration(self):
        audio_file = os.path.join(self.test_dir, "test_audio.wav")
        
        duration = get_audio_duration(audio_file)
        self.assertGreater(duration, 0)

if __name__ == '__main__':
    unittest.main()
            
