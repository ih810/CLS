import argparse
import os
from src.audio.extractor import extract_audio
from src.audio.diarization import SpeakerDiarizer
from src.utils.file_operation import ensure_dir
from src.config.settings import INPUT_DIR, OUTPUT_DIR

def parse_arguments():
    parser = argparse.ArgumentParser(description="Extract audio and perform speaker diarization.")
    parser.add_argument('-i', '--input', help="Input video file", required=True)
    parser.add_argument('-o', '--output', help="Output directory", required=True)
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # Ensure output directory exists
    ensure_dir(args.output)
    print(os.getenv("HUGGING_FACE_TOKEN"))
    # Extract audio
    audio_file = os.path.join(args.output, "extracted_audio.wav")
    extract_audio(args.input, audio_file)
    print(f"Audio extracted: {audio_file}")
    
    # Perform diarization
    auth_token = os.getenv('HUGGING_FACE_TOKEN')
    if not auth_token:
        raise ValueError("Please set the HUGGING_FACE_TOKEN environment variable")
    
    diarizer = SpeakerDiarizer(auth_token)
    speaker_segments = diarizer.diarize(audio_file)
    
    print("Speaker diarization completed.")
    for speaker, segments in speaker_segments.items():
        print(f"Speaker {speaker}: {len(segments)} segments")

if __name__ == "__main__":
    main()
