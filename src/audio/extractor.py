import ffmpeg
from src.config.settings import AUDIO_CODEC, AUDIO_BITRATE

def extract_audio(input_file, output_file):
    try:
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, output_file, acodec=AUDIO_CODEC, audio_bitrate=AUDIO_BITRATE)
        ffmpeg.run(stream, overwrite_output=True, capture_stderr=True)
        print(f"Audio extracted success: {output_file}")
    except ffmpeg.Error as e:
        print(f"Error occurred while extracting audio from {input_file}")
        print(f"Error message: {e.stderr.decode()}")
        raise

def get_audio_duration(file_path):
    try:
        probe = ffmpeg.probe(file_path)
        audio_stream = next((stream for stream in probe['streams'] if stream['code_type'] == 'audio'),None)
        if audio_stream:
            return float(audio_stream['duration'])
        else: 
            print(f"No Audio stream found in {file_path}")
            return 0
    except ffmpeg.Error as e:
        print(f"An error occurred while getting audio duration for {file_path}")
        print(f"Error message: {e.stderr.decode()}")
        raise


