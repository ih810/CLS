import os
import shutil
from src.config.settings import SUPPORTED_VIDEO_FORMATS

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def is_video_file(filename):
    return filename.lower().endswith(SUPPORTED_VIDEO_FORMATS)

def list_video_files(directory):
    video_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if is_video_file(file):
                video_files.append(os.path.join(root, file))
    return video_files

def safe_file_name(filename):
    unsafe_chars = '<>:"/\\|>*'
    for char in unsafe_chars:
        filename = filename.replace(char, '_')
    return filename

def copy_file(src, dst):
    try:
        shutil.copy2(src, dst)
        print(f'Copied {src} to {dst}')
    except IOError as e:
        print(f'unable to copy {e}')
        raise
