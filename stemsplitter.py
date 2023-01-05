import spleeter
from spleeter.separator import Separator

audio_file = 'audio/audio.wav'

# Create a Spleeter separator object
separator = spleeter.Separator('spleeter:5stems')

# Separate the audio into stems
stems = separator.separate(audio_file)

# Save the stems to audio files
stems.export()
