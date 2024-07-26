from pyannote.audio import Pipeline
import torch

class SpeakerDiarizer:
    def __init__(self, auth_token):
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
                                                 use_auth_token=auth_token)
        
    def diarize(self, audio_file):
        """
        Perform speaker diarization on an audio file.
        
        Args:
        audio_file (str): Path to the audio file.
        
        Returns:
        dict: A dictionary where keys are speaker labels and values are lists of speech segments.
        """
        diarization = self.pipeline(audio_file)
        
        speakers = {}
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            if speaker not in speakers:
                speakers[speaker] = []
            speakers[speaker].append({
                'start': turn.start,
                'end': turn.end
            })
        
        return speakers

# The segment_audio method remains the same as in the previous example
